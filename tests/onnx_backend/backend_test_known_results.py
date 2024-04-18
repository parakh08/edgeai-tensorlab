"""
Python lists documenting failing test cases
TODO: Categorize the failing test cases for easier debug
"""


# Fail when TIDL offload is disabled 
cpu_failing_node_tests = ['test_sequence_insert_at_back', \
'test_sequence_map_add_1_sequence_1_tensor', \
'test_identity_opt', \
'test_optional_has_element_optional_input', \
'test_optional_has_element_tensor_input', \
'test_if_seq', \
'test_identity_sequence', \
'test_sequence_map_add_1_sequence_1_tensor_expanded', \
'test_sequence_map_add_2_sequences', \
'test_loop13_seq', \
'test_loop16_seq_none', \
'test_sequence_map_identity_1_sequence_expanded', \
'test_sequence_insert_at_front', \
'test_sequence_map_identity_2_sequences_expanded', \
'test_optional_get_element_optional_sequence', \
'test_optional_get_element_optional_tensor', \
'test_sequence_map_identity_1_sequence_1_tensor', \
'test_optional_get_element_sequence', \
'test_sequence_map_identity_1_sequence_1_tensor_expanded', \
'test_sequence_map_extract_shapes', \
'test_sequence_map_identity_1_sequence', \
'test_sequence_map_add_2_sequences_expanded', \
'test_optional_has_element_empty_optional_input', \
'test_sequence_map_extract_shapes_expanded', \
'test_if_opt', \
'test_sequence_map_identity_2_sequences']

# Fail during compilation
compilation_failing_node_tests = ['test_cast_FLOAT16_to_DOUBLE',\
'test_layer_normalization_2d_axis1_expanded',\
'test_nllloss_NCd1_expanded',\
'test_reshape_one_dim',\
'test_hardsigmoid_default_expanded_ver18',\
'test_layer_normalization_2d_axis_negative_2_expanded',\
'test_transpose_all_permutations_5',\
'test_bernoulli_seed_expanded',\
'test_optional_has_element_empty_optional_input',\
'test_relu_expanded_ver18',\
'test_elu',\
'test_nllloss_NCd1_ii_expanded',\
'test_layer_normalization_3d_axis0_epsilon_expanded',\
'test_sequence_map_identity_1_sequence_1_tensor',\
'test_layer_normalization_2d_axis1_expanded_ver18',\
'test_clip_inbounds',\
'test_globalaveragepool',\
'test_sigmoid',\
'test_leakyrelu_example_expanded',\
'test_castlike_STRING_to_FLOAT',\
'test_layer_normalization_3d_axis0_epsilon_expanded_ver18',\
'test_leakyrelu_example',\
'test_layer_normalization_4d_axis3_expanded_ver18',\
'test_center_crop_pad_crop_and_pad_expanded',\
'test_sce_NCd1d2d3d4d5_mean_weight_log_prob_expanded',\
'test_concat_3d_axis_2',\
'test_layer_normalization_3d_axis_negative_2_epsilon_expanded_ver18',\
'test_averagepool_2d_precomputed_strides',\
'test_flatten_negative_axis4',\
'test_mul_example',\
'test_if_opt',\
'test_thresholdedrelu_example_expanded_ver18',\
'test_cast_DOUBLE_to_FLOAT16',\
'test_concat_2d_axis_negative_2',\
'test_reduce_mean_negative_axes_keepdims_example',\
'test_nllloss_NCd1d2_with_weight_reduction_sum_expanded',\
'test_flatten_negative_axis3',\
'test_layer_normalization_2d_axis0_expanded',\
'test_concat_2d_axis_negative_1',\
'test_clip',\
'test_sequence_map_identity_2_sequences',\
'test_nllloss_NCd1d2d3_sum_weight_high_ii',\
'test_concat_3d_axis_negative_3',\
'test_flatten_axis2',\
'test_logsoftmax_example_1_expanded',\
'test_clip_default_int8_inbounds',\
'test_castlike_FLOAT_to_FLOAT16',\
'test_concat_3d_axis_negative_2',\
'test_reshape_zero_dim',\
'test_cast_FLOAT_to_FLOAT16',\
'test_split_equal_parts_2d',\
'test_hardswish',\
'test_scatternd_multiply',\
'test_mish',\
'test_clip_example',\
'test_leakyrelu_default',\
'test_castlike_FLOAT16_to_FLOAT_expanded',\
'test_layer_normalization_3d_axis2_epsilon_expanded_ver18',\
'test_add_uint8',\
'test_tanh_example',\
'test_nllloss_NCd1d2_reduction_mean',\
'test_hannwindow_expanded',\
'test_scatternd',\
'test_leakyrelu',\
'test_split_zero_size_splits_opset18',\
'test_prelu_broadcast_expanded',\
'test_sequence_insert_at_front',\
'test_reduce_mean_keepdims_example',\
'test_split_equal_parts_1d_opset18',\
'test_reduce_mean_keepdims_random',\
'test_prelu_broadcast',\
'test_concat_2d_axis_1',\
'test_cast_DOUBLE_to_FLOAT',\
'test_averagepool_2d_precomputed_pads_count_include_pad',\
'test_reduce_sum_square_do_not_keepdims_random_expanded',\
'test_hannwindow_symmetric_expanded',\
'test_castlike_FLOAT_to_DOUBLE_expanded',\
'test_flatten_default_axis',\
'test_softmax_large_number',\
'test_castlike_DOUBLE_to_FLOAT',\
'test_layer_normalization_3d_axis_negative_1_epsilon_expanded',\
'test_hammingwindow_expanded',\
'test_slice_default_axes',\
'test_scatternd_max',\
'test_depthtospace_crd_mode_example',\
'test_reduce_sum_square_default_axes_keepdims_example_expanded',\
'test_softmax_example_expanded',\
'test_optional_has_element_tensor_input',\
'test_div',\
'test_nllloss_NCd1d2_no_weight_reduction_mean_ii',\
'test_logsoftmax_default_axis_expanded',\
'test_div_example',\
'test_nllloss_NCd1d2_with_weight_reduction_mean',\
'test_argmax_keepdims_example',\
'test_elu_default',\
'test_layer_normalization_2d_axis0_expanded_ver18',\
'test_gemm_default_matrix_bias',\
'test_layer_normalization_4d_axis_negative_2_expanded',\
'test_loop11',\
'test_clip_default_min',\
'test_reshape_reduced_dims',\
'test_reduce_log_sum_exp_do_not_keepdims_random_expanded',\
'test_resize_upsample_scales_nearest',\
'test_hardsigmoid_expanded_ver18',\
'test_nllloss_NCd1d2_with_weight_reduction_sum_ii',\
'test_layer_normalization_4d_axis_negative_4_expanded_ver18',\
'test_nllloss_NCd1d2_no_weight_reduction_mean_ii_expanded',\
'test_group_normalization_example_expanded',\
'test_clip_default_max',\
'test_depthtospace_example',\
'test_quantizelinear_axis',\
'test_layer_normalization_4d_axis2_expanded_ver18',\
'test_castlike_STRING_to_FLOAT_expanded',\
'test_nllloss_NCd1_mean_weight_negative_ii_expanded',\
'test_sequence_map_identity_1_sequence_expanded',\
'test_matmul_3d',\
'test_cast_FLOAT16_to_FLOAT',\
'test_castlike_DOUBLE_to_FLOAT16_expanded',\
'test_loop13_seq',\
'test_nllloss_NCd1',\
'test_split_equal_parts_default_axis_opset13',\
'test_matmul_2d',\
'test_blackmanwindow_expanded',\
'test_center_crop_pad_crop_axes_hwc_expanded',\
'test_sub_example',\
'test_flatten_axis1',\
'test_resize_upsample_scales_linear',\
'test_slice_default_steps',\
'test_resize_downsample_sizes_linear_pytorch_half_pixel',\
'test_batchnorm_example',\
'test_layer_normalization_3d_axis_negative_1_epsilon_expanded_ver18',\
'test_clip_outbounds',\
'test_layer_normalization_3d_axis_negative_2_epsilon_expanded',\
'test_group_normalization_epsilon',\
'test_softplus_expanded',\
'test_maxpool_2d_precomputed_same_upper',\
'test_layer_normalization_4d_axis1_expanded',\
'test_nllloss_NCd1d2d3_none_no_weight_negative_ii_expanded',\
'test_dequantizelinear_axis',\
'test_hardsigmoid_default',\
'test_layer_normalization_4d_axis_negative_3_expanded',\
'test_reduce_log_sum_exp_negative_axes_keepdims_example_expanded',\
'test_logsoftmax_axis_1_expanded',\
'test_center_crop_pad_crop_axes_hwc',\
'test_cast_FLOAT_to_DOUBLE',\
'test_averagepool_2d_precomputed_pads',\
'test_center_crop_pad_crop',\
'test_reduce_mean_negative_axes_keepdims_random',\
'test_nllloss_NCd1_weight',\
'test_nllloss_NCd1d2_with_weight_reduction_sum_ii_expanded',\
'test_sce_NCd1d2d3d4d5_none_no_weight_log_prob_expanded',\
'test_split_variable_parts_default_axis_opset13',\
'test_nllloss_NCd1_ii',\
'test_reduce_sum_square_do_not_keepdims_example_expanded',\
'test_clip_default_inbounds_expanded',\
'test_softmax_default_axis_expanded',\
'test_optional_get_element_sequence',\
'test_batchnorm_epsilon',\
'test_layer_normalization_3d_axis1_epsilon_expanded',\
'test_bernoulli',\
'test_split_variable_parts_default_axis_opset18',\
'test_sequence_map_identity_1_sequence_1_tensor_expanded',\
'test_split_variable_parts_1d_opset18',\
'test_div_uint8',\
'test_softmax_negative_axis',\
'test_slice_neg_steps',\
'test_identity',\
'test_hardsigmoid_example',\
'test_logsoftmax_negative_axis_expanded',\
'test_bernoulli_expanded',\
'test_layer_normalization_2d_axis_negative_1_expanded_ver18',\
'test_transpose_all_permutations_1',\
'test_concat_3d_axis_0',\
'test_castlike_FLOAT16_to_DOUBLE',\
'test_nllloss_NCd1_weight_expanded',\
'test_bernoulli_double',\
'test_sce_NCd1d2d3d4d5_none_no_weight_expanded',\
'test_reshape_reordered_all_dims',\
'test_resize_downsample_sizes_nearest',\
'test_center_crop_pad_crop_expanded',\
'test_thresholdedrelu_default_expanded_ver18',\
'test_identity_sequence',\
'test_dequantizelinear',\
'test_averagepool_2d_precomputed_same_upper',\
'test_layer_normalization_4d_axis_negative_1_expanded',\
'test_resize_downsample_scales_linear_align_corners',\
'test_center_crop_pad_pad',\
'test_upsample_nearest',\
'test_split_equal_parts_default_axis_opset18',\
'test_split_equal_parts_1d_opset13',\
'test_nllloss_NCd1d2d3d4d5_mean_weight',\
'test_thresholdedrelu_expanded_ver18',\
'test_nllloss_NCd1d2_reduction_sum',\
'test_logsoftmax_axis_2_expanded',\
'test_castlike_FLOAT_to_DOUBLE',\
'test_cast_FLOAT_to_STRING',\
'test_nllloss_NCd1_mean_weight_negative_ii',\
'test_reduce_sum_square_keepdims_random_expanded',\
'test_gemm_default_vector_bias',\
'test_resize_upsample_sizes_nearest',\
'test_bernoulli_seed',\
'test_sub_bcast',\
'test_sub',\
'test_group_normalization_epsilon_expanded',\
'test_split_variable_parts_2d_opset13',\
'test_argmax_no_keepdims_random',\
'test_maxpool_2d_precomputed_strides',\
'test_sequence_map_add_2_sequences_expanded',\
'test_split_zero_size_splits_opset13',\
'test_nllloss_NCd1_weight_ii',\
'test_scan9_sum',\
'test_gemm_default_single_elem_vector_bias',\
'test_castlike_FLOAT_to_FLOAT16_expanded',\
'test_center_crop_pad_pad_expanded',\
'test_castlike_FLOAT_to_STRING',\
'test_reduce_sum_square_default_axes_keepdims_random_expanded',\
'test_layer_normalization_3d_axis_negative_3_epsilon_expanded',\
'test_reduce_sum_square_negative_axes_keepdims_example_expanded',\
'test_constant_pad_axes',\
'test_slice_neg',\
'test_castlike_FLOAT16_to_FLOAT',\
'test_transpose_default',\
'test_slice_negative_axes',\
'test_reduce_mean_default_axes_keepdims_random',\
'test_softmax_axis_2',\
'test_layer_normalization_4d_axis0_expanded_ver18',\
'test_mul_uint8',\
'test_optional_get_element_optional_tensor',\
'test_bernoulli_double_expanded',\
'test_nllloss_NCd1d2_with_weight_reduction_sum',\
'test_hardsigmoid',\
'test_gemm_default_no_bias',\
'test_blackmanwindow_symmetric_expanded',\
'test_nllloss_NCd1d2d3_none_no_weight_negative_ii',\
'test_mish_expanded',\
'test_flatten_axis0',\
'test_scatter_elements_with_negative_indices',\
'test_layer_normalization_4d_axis_negative_2_expanded_ver18',\
'test_sqrt_example',\
'test_reshape_negative_dim',\
'test_reduce_log_sum_exp_keepdims_example_expanded',\
'test_castlike_DOUBLE_to_FLOAT_expanded',\
'test_softmax_negative_axis_expanded',\
'test_sequence_insert_at_back',\
'test_scatternd_add',\
'test_nllloss_NCd1d2d3d4d5_none_no_weight',\
'test_split_variable_parts_1d_opset13',\
'test_reduce_sum_square_negative_axes_keepdims_random_expanded',\
'test_resize_upsample_scales_linear_align_corners',\
'test_nllloss_NC',\
'test_transpose_all_permutations_2',\
'test_layer_normalization_2d_axis_negative_1_expanded',\
'test_reduce_log_sum_exp_negative_axes_keepdims_random_expanded',\
'test_layer_normalization_4d_axis1_expanded_ver18',\
'test_softmax_default_axis',\
'test_globalaveragepool_precomputed',\
'test_castlike_FLOAT_to_STRING_expanded',\
'test_reduce_mean_default_axes_keepdims_example',\
'test_div_bcast',\
'test_center_crop_pad_crop_axes_chw_expanded',\
'test_transpose_all_permutations_3',\
'test_sequence_map_identity_1_sequence',\
'test_flatten_negative_axis2',\
'test_reduce_mean_do_not_keepdims_random',\
'test_clip_default_inbounds',\
'test_layer_normalization_3d_axis2_epsilon_expanded',\
'test_sequence_map_add_1_sequence_1_tensor_expanded',\
'test_cast_BFLOAT16_to_FLOAT',\
'test_sce_NCd1d2d3d4d5_mean_weight_expanded',\
'test_hardsigmoid_example_expanded_ver18',\
'test_sum_two_inputs',\
'test_sequence_map_extract_shapes_expanded',\
'test_constant_pad',\
'test_mvn_expanded',\
'test_cast_STRING_to_FLOAT',\
'test_scatternd_min',\
'test_layer_normalization_default_axis_expanded',\
'test_layer_normalization_4d_axis_negative_1_expanded_ver18',\
'test_logsoftmax_large_number_expanded',\
'test_argmax_keepdims_random',\
'test_pow_types_float32_int32',\
'test_reshape_reordered_last_dims',\
'test_sqrt',\
'test_erf',\
'test_reduce_log_sum_exp_default_axes_keepdims_random_expanded',\
'test_softplus_example_expanded',\
'test_hardswish_expanded',\
'test_center_crop_pad_crop_axes_chw',\
'test_concat_1d_axis_0',\
'test_softmax_example',\
'test_nllloss_NCd1d2_reduction_mean_expanded',\
'test_resize_upsample_sizes_nearest_ceil_half_pixel',\
'test_hammingwindow_symmetric_expanded',\
'test_sigmoid_example',\
'test_layer_normalization_4d_axis2_expanded',\
'test_mul',\
'test_maxpool_with_argmax_2d_precomputed_strides',\
'test_sub_uint8',\
'test_reshape_negative_extended_dims',\
'test_gemm_transposeB',\
'test_logsoftmax_axis_0_expanded',\
'test_mvn_expanded_ver18',\
'test_nllloss_NCd1d2_reduction_sum_expanded',\
'test_tanh',\
'test_layer_normalization_3d_axis1_epsilon_expanded_ver18',\
'test_clip_default_int8_min',\
'test_softmax_axis_2_expanded',\
'test_softmax_axis_1_expanded',\
'test_softmax_axis_0_expanded',\
'test_resize_upsample_sizes_nearest_round_prefer_ceil_asymmetric',\
'test_nllloss_NCd1d2_with_weight_expanded',\
'test_split_variable_parts_2d_opset18',\
'test_celu_expanded',\
'test_reduce_log_sum_exp_do_not_keepdims_example_expanded',\
'test_resize_tf_crop_and_resize',\
'test_nllloss_NCd1_weight_ii_expanded',\
'test_layer_normalization_3d_axis_negative_3_epsilon_expanded_ver18',\
'test_flatten_negative_axis1',\
'test_castlike_FLOAT16_to_DOUBLE_expanded',\
'test_gemm_default_scalar_bias',\
'test_elu_example',\
'test_layer_normalization_default_axis_expanded_ver18',\
'test_transpose_all_permutations_4',\
'test_clip_default_int8_inbounds_expanded',\
'test_scan_sum',\
'test_prelu_example',\
'test_nllloss_NC_expanded',\
'test_scatter_elements_with_axis',\
'test_group_normalization_example',\
'test_reshape_zero_and_negative_dim',\
'test_reduce_log_sum_exp_keepdims_random_expanded',\
'test_add',\
'test_optional_has_element_optional_input',\
'test_quantizelinear',\
'test_leakyrelu_default_expanded',\
'test_nllloss_NCd1d2_expanded',\
'test_sequence_map_extract_shapes',\
'test_loop16_seq_none',\
'test_if_seq',\
'test_sequence_map_add_2_sequences',\
'test_reshape_extended_dims',\
'test_nllloss_NCd1d2d3d4d5_mean_weight_expanded',\
'test_averagepool_2d_ceil',\
'test_argmax_no_keepdims_example',\
'test_layer_normalization_4d_axis0_expanded',\
'test_relu',\
'test_gemm_default_zero_bias',\
'test_matmul_4d',\
'test_resize_downsample_scales_nearest',\
'test_resize_downsample_scales_linear',\
'test_layer_normalization_4d_axis_negative_3_expanded_ver18',\
'test_concat_2d_axis_0',\
'test_optional_get_element_optional_sequence',\
'test_nllloss_NCd1d2d3_sum_weight_high_ii_expanded',\
'test_split_equal_parts_2d_opset13',\
'test_split_2d_uneven_split_opset18',\
'test_leakyrelu_expanded',\
'test_split_1d_uneven_split_opset18',\
'test_center_crop_pad_crop_and_pad',\
'test_resize_upsample_sizes_nearest_floor_align_corners',\
'test_slice_start_out_of_bounds',\
'test_nllloss_NCd1d2_with_weight',\
'test_slice_end_out_of_bounds',\
'test_softmax_large_number_expanded',\
'test_clip_splitbounds',\
'test_concat_1d_axis_negative_1',\
'test_layer_normalization_4d_axis_negative_4_expanded',\
'test_identity_opt',\
'test_sequence_map_add_1_sequence_1_tensor',\
'test_reduce_sum_square_keepdims_example_expanded',\
'test_sequence_map_identity_2_sequences_expanded',\
'test_maxpool_2d_ceil',\
'test_softmax_axis_0',\
'test_reduce_mean_do_not_keepdims_example',\
'test_slice',\
'test_softmax_axis_1',\
'test_transpose_all_permutations_0',\
'test_flatten_axis3',\
'test_cast_FLOAT_to_BFLOAT16',\
'test_castlike_DOUBLE_to_FLOAT16',\
'test_concat_3d_axis_negative_1',\
'test_layer_normalization_2d_axis_negative_2_expanded_ver18',\
'test_nllloss_NCd1d2',\
'test_layer_normalization_4d_axis3_expanded',\
'test_concat_3d_axis_1',\
'test_clip_default_int8_max',\
'test_reduce_log_sum_exp_default_axes_keepdims_example_expanded',\
'test_nllloss_NCd1d2_with_weight_reduction_mean_expanded']

# Fail during inference when compilation succeeds
inference_failing_node_tests = ['test_sce_sum',\
'test_sce_none_log_prob',\
'test_simple_rnn_batchwise',\
'test_nesterov_momentum',\
'test_reduce_l2_default_axes_keepdims_example_expanded',\
'test_adam_multiple',\
'test_reduce_l2_keep_dims_example_expanded',\
'test_strnormalizer_nostopwords_nochangecase',\
'test_sce_mean_weight_ii_4d_log_prob',\
'test_sce_NCd1d2d3d4d5_mean_weight_log_prob',\
'test_sce_none_weights',\
'test_sce_mean_no_weight_ii_4d_log_prob_expanded',\
'test_sce_NCd1d2d3_sum_weight_high_ii_log_prob',\
'test_pow_types_float32_uint32',\
'test_castlike_FLOAT_to_BFLOAT16_expanded',\
'test_tfidfvectorizer_tf_onlybigrams_skip5',\
'test_sce_mean_weight_ii_3d_log_prob_expanded',\
'test_castlike_FLOAT_to_BFLOAT16',\
'test_max_int8',\
'test_pow_types_float32_uint64',\
'test_reduce_l2_do_not_keepdims_random_expanded',\
'test_sce_NCd1d2d3_sum_weight_high_ii_expanded',\
'test_sce_NCd1d2d3_none_no_weight_negative_ii',\
'test_strnormalizer_export_monday_insensintive_upper_twodim',\
'test_strnormalizer_export_monday_casesensintive_upper',\
'test_sce_NCd1d2d3d4d5_mean_weight',\
'test_sce_mean_weight_log_prob_expanded',\
'test_sce_mean_weight_expanded',\
'test_sce_mean_weight',\
'test_sce_none_weights_log_prob',\
'test_reduce_l2_negative_axes_keep_dims_random_expanded',\
'test_sce_mean_log_prob_expanded',\
'test_sce_mean',\
'test_elu_example_expanded_ver18',\
'test_sce_NCd1_mean_weight_negative_ii_expanded',\
'test_training_dropout_default',\
'test_sce_none_expanded',\
'test_sce_mean_weight_ii_4d_log_prob_expanded',\
'test_sce_mean_no_weight_ii_4d',\
'test_sce_mean_no_weight_ii_3d',\
'test_range_float_type_positive_delta_expanded',\
'test_momentum',\
'test_sce_mean_expanded',\
'test_softsign_example_expanded_ver18',\
'test_sce_mean_weight_ii_3d_log_prob',\
'test_sce_mean_weight_ii',\
'test_sce_mean_no_weight_ii_3d_log_prob_expanded',\
'test_adagrad_multiple',\
'test_sce_NCd1d2d3d4d5_none_no_weight',\
'test_max_int16',\
'test_training_dropout_default_mask',\
'test_sce_mean_3d_expanded',\
'test_sce_mean_no_weight_ii_log_prob_expanded',\
'test_sce_NCd1_mean_weight_negative_ii',\
'test_max_uint8',\
'test_elu_expanded_ver18',\
'test_adam',\
'test_min_uint8',\
'test_sce_mean_log_prob',\
'test_elu_default_expanded_ver18',\
'test_sce_mean_3d_log_prob_expanded',\
'test_sce_NCd1_mean_weight_negative_ii_log_prob',\
'test_selu_default_expanded_ver18',\
'test_sce_NCd1d2d3_none_no_weight_negative_ii_expanded',\
'test_sce_NCd1d2d3_none_no_weight_negative_ii_log_prob_expanded',\
'test_sce_NCd1d2d3_sum_weight_high_ii_log_prob_expanded',\
'test_min_uint16',\
'test_sce_none',\
'test_reduce_l2_keep_dims_random_expanded',\
'test_sce_mean_no_weight_ii_3d_log_prob',\
'test_max_uint16',\
'test_sce_mean_weight_ii_log_prob_expanded',\
'test_clip_default_int8_min_expanded',\
'test_training_dropout',\
'test_castlike_BFLOAT16_to_FLOAT_expanded',\
'test_sce_sum_log_prob_expanded',\
'test_sce_mean_weight_ii_4d_expanded',\
'test_sce_NCd1_mean_weight_negative_ii_log_prob_expanded',\
'test_momentum_multiple',\
'test_sce_none_weights_log_prob_expanded',\
'test_min_int8',\
'test_maxunpool_export_with_output_shape',\
'test_bitshift_right_uint16',\
'test_lstm_batchwise',\
'test_sce_mean_3d_log_prob',\
'test_sce_mean_no_weight_ii',\
'test_sce_mean_weight_ii_3d_expanded',\
'test_strnormalizer_export_monday_casesensintive_nochangecase',\
'test_sce_mean_weight_ii_log_prob',\
'test_sce_none_log_prob_expanded',\
'test_clip_default_int8_max_expanded',\
'test_reduce_l2_negative_axes_keep_dims_example_expanded',\
'test_sce_NCd1d2d3_sum_weight_high_ii',\
'test_sce_mean_no_weight_ii_4d_expanded',\
'test_gru_batchwise',\
'test_sce_mean_weight_ii_3d',\
'test_sce_sum_expanded',\
'test_strnormalizer_export_monday_casesensintive_lower',\
'test_castlike_BFLOAT16_to_FLOAT',\
'test_range_int32_type_negative_delta_expanded',\
'test_unique_sorted_with_axis',\
'test_sce_mean_no_weight_ii_4d_log_prob',\
'test_sce_mean_no_weight_ii_expanded',\
'test_sce_sum_log_prob',\
'test_sce_mean_3d',\
'test_shrink_hard_expanded_ver18',\
'test_training_dropout_mask',\
'test_softsign_expanded_ver18',\
'test_selu_example_expanded_ver18',\
'test_sce_none_weights_expanded',\
'test_sce_mean_no_weight_ii_3d_expanded',\
'test_prelu_example_expanded',\
'test_reduce_l2_default_axes_keepdims_random_expanded',\
'test_sce_mean_weight_log_prob',\
'test_strnormalizer_export_monday_empty_output',\
'test_bitshift_left_uint16',\
'test_adagrad',\
'test_shrink_soft_expanded_ver18',\
'test_min_int16',\
'test_selu_expanded_ver18',\
'test_sce_mean_weight_ii_4d',\
'test_sce_mean_no_weight_ii_log_prob',\
'test_sce_NCd1d2d3d4d5_none_no_weight_log_prob',\
'test_sce_NCd1d2d3_none_no_weight_negative_ii_log_prob',\
'test_sce_mean_weight_ii_expanded',\
'test_reduce_l2_do_not_keepdims_example_expanded']