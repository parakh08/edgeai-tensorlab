# Copyright (c) 2018-2021, Texas Instruments
# All Rights Reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import sys
import argparse
import yaml
from edgeai_benchmark import *


if __name__ == '__main__':
    print(f'argv: {sys.argv}')
    # the cwd must be the root of the respository
    if os.path.split(os.getcwd())[-1] == 'scripts':
        os.chdir('../')
    #

    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument('settings_file', type=str, default=None)
    parser.add_argument('--target_device', type=str)
    parser.add_argument('--tensor_bits', type=utils.str_to_int)
    parser.add_argument('--configs_path', type=str)
    parser.add_argument('--models_path', type=str)
    parser.add_argument('--task_selection', type=str, nargs='*')
    parser.add_argument('--runtime_selection', type=str, nargs='*')
    parser.add_argument('--model_selection', type=str, nargs='*')
    parser.add_argument('--model_shortlist', type=utils.int_or_none)
    parser.add_argument('--session_type_dict', type=str, nargs='*')
    parser.add_argument('--num_frames', type=int)
    parser.add_argument('--calibration_frames', type=int)
    parser.add_argument('--calibration_iterations', type=int)
    parser.add_argument('--run_import', type=utils.str_to_bool)
    parser.add_argument('--run_inference', type=utils.str_to_bool)
    parser.add_argument('--modelartifacts_path', type=str)
    parser.add_argument('--modelpackage_path', type=str)
    parser.add_argument('--dataset_loading', type=str, nargs='*')
    parser.add_argument('--parallel_devices', type=utils.int_or_none)
    parser.add_argument('--parallel_processes', type=int)
    parser.add_argument('--fast_calibration_factor', type=utils.float_or_none)
    parser.add_argument('--experimental_models', type=utils.str_to_bool)
    parser.add_argument('--param_template_file', type=str, default='./examples/configs/yaml/param_template.yaml')
    cmds = parser.parse_args()

    kwargs = vars(cmds)
    if 'session_type_dict' in kwargs:
        kwargs['session_type_dict'] = utils.str_to_dict(kwargs['session_type_dict'])
    #
    settings = config_settings.ConfigSettings(cmds.settings_file, **kwargs)
    print(f'settings: {settings}')
    sys.stdout.flush()

    work_dir = os.path.join(settings.modelartifacts_path, f'{settings.tensor_bits}bits')
    print(f'work_dir: {work_dir}')

    settings.pipeline_type = constants.PIPELINE_GEN_CONFIG
    settings.param_template_file = settings.param_template_file or cmds.param_template_file
    settings.dataset_loading = False
    settings.input_optimization = False
    if 'TIDL_TOOLS_PATH' not in os.environ:
        os.environ['TIDL_TOOLS_PATH'] = ""

    # run the pipeline
    results_list = interfaces.run_gen_config(settings, work_dir)

    models_path_full = os.path.normpath(os.path.abspath(settings.models_path))

    configs_dict={'configs': {}}
    for result_dict in results_list:
        if result_dict:
           config_path = result_dict['config_path']
           with open(config_path) as fp:
               config_dict = yaml.safe_load(fp)
           #
           model_id = config_dict['session']['model_id']
           config_path = os.path.normpath(os.path.abspath(config_path))
           config_path = config_path.replace(models_path_full+os.sep, '')
           configs_dict['config_paths'][model_id] = config_path

    configlist_path = os.path.join(settings.models_path, 'configs.yaml')
    with open(configlist_path, 'w') as fp:
        yaml.safe_dump(configs_dict, fp, sort_keys=False)
    #