
import functools
import math
import random
import torch
from torch.ao.quantization import MinMaxObserver, PerChannelMinMaxObserver, HistogramObserver, \
    MovingAverageMinMaxObserver, MovingAveragePerChannelMinMaxObserver

from .... import xnn
from . import observer_utils


####################################################################
# select which histogram observer to use in this file as the base

# FastHistogramObserver = observer_utils.MSEHistogramObserverBase
# MovingAverageFastHistogramObserver = observer_utils.MovingAverageMSEHistogramObserverBase

FastHistogramObserver = observer_utils.RangeShrinkHistogramObserverBase
MovingAverageFastHistogramObserver = observer_utils.MovingAverageRangeShrinkHistogramObserverBase


####################################################################
class AdaptiveWeightObserver(FastHistogramObserver):
    def __init__(self, *args, quant_min=None, quant_max=None, dtype=None, qscheme=None, power2=False, range_max=None, fixed_range=False, **kwargs):
        quant_min = quant_min or -128
        quant_max = quant_max or +127
        dtype = dtype or torch.qint8
        qscheme = qscheme or torch.per_tensor_symmetric
        super().__init__(*args, quant_min=quant_min, quant_max=quant_max, dtype=dtype, qscheme=qscheme, **kwargs)
        self.power2 = power2
        self.range_max = range_max
        self.fixed_range = fixed_range
        self.quant_min_orig = self.quant_min
        self.quant_max_orig = self.quant_max

    @torch.jit.export
    def _calculate_qparams(self, min_val, max_val):
        r"""Calculates the quantization parameters."""
        if not self.power2:
            return super()._calculate_qparams(min_val, max_val)
        else:
            self.quant_min = observer_utils.ceil2_num(self.quant_min_orig)
            self.quant_max = observer_utils.ceil2_num(self.quant_max_orig)
            qparams = super()._calculate_qparams(observer_utils.ceil2_tensor(min_val), observer_utils.ceil2_tensor(max_val))
            self.quant_min, self.quant_max = self.quant_min_orig, self.quant_max_orig
            return qparams

    def forward(self, x_orig):
        x_orig = super().forward(x_orig)
        if self.range_max is not None:
            signed_range = torch.min(self.min_val.detach()).item() < 0.0
            min_val = (-self.range_max) if signed_range else 0.0
            max_val = (+self.range_max) if signed_range else (+self.range_max)
            if self.fixed_range:
                self.min_val.fill_(min_val)
                self.max_val.fill_(max_val)
            else:
                self.min_val = torch.clamp(self.min_val, min=min_val, max=0.0)
                self.max_val = torch.clamp(self.max_val, min=0.0, max=max_val)
            #
        #
        return x_orig


class AdaptivePerChannelWeightObserver(PerChannelMinMaxObserver):
    def __init__(self, *args, quant_min=None, quant_max=None, dtype=None, qscheme=None, power2=False, range_max=None, fixed_range=False, **kwargs):
        quant_min = quant_min or -128
        quant_max = quant_max or +127
        dtype = dtype or torch.qint8
        qscheme = qscheme or torch.per_channel_symmetric
        super().__init__(*args, quant_min=quant_min, quant_max=quant_max, dtype=dtype, qscheme=qscheme, **kwargs)
        self.power2 = power2
        self.fixed_range = fixed_range
        self.range_max = range_max
        self.quant_min_orig = self.quant_min
        self.quant_max_orig = self.quant_max

    @torch.jit.export
    def _calculate_qparams(self, min_val, max_val):
        r"""Calculates the quantization parameters."""
        if not self.power2:
            return super()._calculate_qparams(min_val, max_val)
        else:
            self.quant_min = observer_utils.ceil2_num(self.quant_min_orig)
            self.quant_max = observer_utils.ceil2_num(self.quant_max_orig)
            qparams = super()._calculate_qparams(observer_utils.ceil2_tensor(min_val), observer_utils.ceil2_tensor(max_val))
            self.quant_min, self.quant_max = self.quant_min_orig, self.quant_max_orig
            return qparams

    def forward(self, x_orig):
        x_orig = super().forward(x_orig)
        if self.range_max is not None:
            signed_range = torch.min(self.min_val.detach()).item() < 0.0
            min_val = (-self.range_max) if signed_range else 0.0
            max_val = (+self.range_max) if signed_range else (+self.range_max)
            if self.fixed_range:
                self.min_val.fill_(min_val)
                self.max_val.fill_(max_val)
            else:
                self.min_val = torch.clamp(self.min_val, min=min_val, max=0.0)
                self.max_val = torch.clamp(self.max_val, min=0.0, max=max_val)
            #
        #
        return x_orig


class AdaptiveActivationObserver(MovingAverageFastHistogramObserver):
    def __init__(self, *args, quant_min=None, quant_max=None, dtype=None, qscheme=None, power2=False, range_max=None, **kwargs):
        quant_min = quant_min or 0
        quant_max = quant_max or 255
        dtype = dtype or torch.quint8
        qscheme = qscheme or torch.per_tensor_affine
        super().__init__(*args, quant_min=quant_min, quant_max=quant_max, dtype=dtype, qscheme=qscheme, **kwargs)
        self.power2 = power2
        self.range_max = range_max

    @torch.jit.export
    def _calculate_qparams(self, min_val, max_val):
        r"""Calculates the quantization parameters."""
        if not self.power2:
            return super()._calculate_qparams(min_val, max_val)
        else:
            quant_min_orig, quant_max_orig = self.quant_min, self.quant_max
            self.quant_min, self.quant_max = observer_utils.ceil2_num(self.quant_min), observer_utils.ceil2_num(self.quant_max)
            qparams = super()._calculate_qparams(observer_utils.ceil2_tensor(min_val), observer_utils.ceil2_tensor(max_val))
            self.quant_min, self.quant_max = quant_min_orig, quant_max_orig
            return qparams

    def forward(self, x_orig):
        x_orig = super().forward(x_orig)
        if self.range_max is not None:
            signed_range = torch.min(self.min_val.detach()).item() < 0.0
            min_val = (-self.range_max) if signed_range else 0.0
            max_val = (+self.range_max) if signed_range else (+self.range_max)
            if self.fixed_range:
                self.min_val.fill_(min_val)
                self.max_val.fill_(max_val)
            else:
                self.min_val = torch.clamp(self.min_val, min=min_val, max=0.0)
                self.max_val = torch.clamp(self.max_val, min=0.0, max=max_val)
            #
        #
        return x_orig


####################################################################
ADAPTIVE_WEIGHT_OBSERVER_TYPES = (AdaptiveWeightObserver,
                                  AdaptivePerChannelWeightObserver)

ADAPTIVE_ACTIVATION_OBSERVER_TYPES = (AdaptiveActivationObserver,)

ADAPTIVE_OBSERVER_TYPES = tuple(list(ADAPTIVE_WEIGHT_OBSERVER_TYPES) + list(ADAPTIVE_ACTIVATION_OBSERVER_TYPES))


####################################################################
# additional derived observers
AdaptivePower2WeightObserver = xnn.utils.partialclass(AdaptiveWeightObserver, power2=True, class_name='AdaptivePower2WeightObserver')
AdaptivePerChannelPower2WeightObserver = xnn.utils.partialclass(AdaptivePerChannelWeightObserver, power2=True, class_name='AdaptivePerChannelPower2WeightObserver')
AdaptivePerChannelBit4WeightObserver = xnn.utils.partialclass(AdaptivePerChannelWeightObserver, quant_min=-8, quant_max=7, class_name='AdaptivePerChannelBit4WeightObserver')
AdaptivePerChannelBit4MaxRange4WeightObserver = xnn.utils.partialclass(AdaptivePerChannelWeightObserver, quant_min=-8, quant_max=7, range_max=4.0, class_name='AdaptivePerChannelBit4MaxRange4WeightObserver')
AdaptivePerChannelBit4FixedRange4WeightObserver = xnn.utils.partialclass(AdaptivePerChannelWeightObserver, quant_min=-8, quant_max=7, range_max=4.0, fixed_range=True, class_name='AdaptivePerChannelBit4FixedRange4WeightObserver')

AdaptivePower2ActivationObserver = xnn.utils.partialclass(AdaptiveActivationObserver, power2=True, class_name='AdaptivePower2ActivationObserver')
AdaptiveBit4ActivationObserver = xnn.utils.partialclass(AdaptiveActivationObserver, quant_min=0, quant_max=15, class_name='AdaptiveBit4ActivationObserver')
AdaptiveBit4MaxRange4ActivationObserver = xnn.utils.partialclass(AdaptiveActivationObserver, quant_min=0, quant_max=15, range_max=4.0, class_name='AdaptiveBit4MaxRange4ActivationObserver')
AdaptiveBit4FixedRange4ActivationObserver = xnn.utils.partialclass(AdaptiveActivationObserver, quant_min=0, quant_max=15, range_max=4.0, fixed_range=True, class_name='AdaptiveBit4FixedRange4ActivationObserver')
