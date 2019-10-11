[cfg_proto]
cfg_proto = proto/global.proto
cfg_proto_chunk = proto/global_chunk.proto

[exp]
cmd =
run_nn_script = run_nn.py
out_folder = exp/SincNet33333
pretrain_file = none
seed = 1234
use_cuda = True
multi_gpu = False
save_gpumem = True
n_epochs_tr = 25
nr_of_valid_per_epoch = 1

[dataset1]
data_name = TIMIT_tr    
fea =   fea_name=raw
    fea_lst=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/raw_timit/train/feats_raw.scp
    fea_opts=
    cw_left=0
    cw_right=0
lab = lab_name=lab_cd
    lab_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/dnn4_pretrain-dbn_dnn_ali
    lab_opts=ali-to-pdf
    lab_count_file=auto
    lab_data_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/train/
    lab_graph=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/tri3/graph
    
    lab_name=lab_mono
    lab_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/dnn4_pretrain-dbn_dnn_ali
    lab_opts=ali-to-phones --per-frame=true
    lab_count_file=none
    lab_data_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/train/
    lab_graph=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/tri3/graph
n_chunks = 10

[dataset2]
data_name = TIMIT_dev
fea =   fea_name=raw
    fea_lst=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/raw_timit/dev/feats_raw.scp
    fea_opts=
    cw_left=0
    cw_right=0
lab = lab_name=lab_cd
    lab_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/dnn4_pretrain-dbn_dnn_ali_dev
    lab_opts=ali-to-pdf
    lab_count_file=auto
    lab_data_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/dev/
    lab_graph=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/tri3/graph

    lab_name=lab_mono
    lab_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/dnn4_pretrain-dbn_dnn_ali_dev
    lab_opts=ali-to-phones --per-frame=true
    lab_count_file=none
    lab_data_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/dev/
    lab_graph=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/tri3/graph
n_chunks = 2 

[dataset3]
data_name = TIMIT_test
fea =   fea_name=raw
    fea_lst=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/raw_timit/test/feats_raw.scp
    fea_opts=
    cw_left=0
    cw_right=0
lab = lab_name=lab_cd
    lab_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/dnn4_pretrain-dbn_dnn_ali_test
    lab_opts=ali-to-pdf
    lab_count_file=auto
    lab_data_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/test/
    lab_graph=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/tri3/graph

    lab_name=lab_mono
    lab_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/dnn4_pretrain-dbn_dnn_ali_test
    lab_opts=ali-to-phones --per-frame=true
    lab_count_file=none
    lab_data_folder=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/data/test/
    lab_graph=/local_disk/zephyr2/pgnoe/kaldi/egs/timit/s5/exp/tri3/graph
n_chunks = 2



[data_use]
train_with = TIMIT_tr
valid_with = TIMIT_dev
forward_with = TIMIT_test

[batches]
batch_size_train = 128
max_seq_length_train = 1000
increase_seq_length_train = False
start_seq_len_train = 100
multply_factor_seq_len_train = 2
batch_size_valid = 128
max_seq_length_valid = 1000

[architecture1]
arch_name = CNN_layers
arch_proto = proto/SincNet.proto
arch_library = neural_networks
arch_class = SincNet
arch_pretrain_file = none
arch_freeze = False
arch_seq_model = False
sinc_n_filt = 128,120,120,120
sinc_len_filt = 129,5,5,3
sinc_max_pool_len = 3,3,3,2
sinc_use_laynorm_inp = True
sinc_use_batchnorm_inp = False
sinc_use_laynorm = False,False,False,False
sinc_use_batchnorm = False,False,False,False
sinc_act = relu,relu,relu,relu
sinc_drop = 0.15,0.15,0.15,0.15
sinc_sample_rate = 16000
sinc_min_low_hz = 50
sinc_min_band_hz = 50
arch_lr = 0.0008
arch_halving_factor = 0.5
arch_improvement_threshold = 0.001
arch_opt = rmsprop
opt_momentum = 0.0
opt_alpha = 0.95
opt_eps = 1e-8
opt_centered = False
opt_weight_decay = 0.0

[architecture2]
arch_name = MLP_layers
arch_proto = proto/MLP.proto
arch_library = neural_networks
arch_class = MLP
arch_pretrain_file = none
arch_freeze = False
arch_seq_model = False
dnn_lay = 1330,1330,1330,1330,1330
dnn_drop = 0.15,0.15,0.15,0.15,0.15
dnn_use_laynorm_inp = False
dnn_use_batchnorm_inp = False
dnn_use_batchnorm = True,True,True,True,True
dnn_use_laynorm = False,False,False,False,False
dnn_act = relu,relu,relu,relu,relu
arch_lr = 0.08
arch_halving_factor = 0.5
arch_improvement_threshold = 0.001
arch_opt = sgd
opt_momentum = 0.0
opt_weight_decay = 0.0
opt_dampening = 0.0
opt_nesterov = False


[architecture3]
arch_name = MLP_soft1
arch_proto = proto/MLP.proto
arch_library = neural_networks
arch_class = MLP
arch_pretrain_file = none
arch_freeze = False
arch_seq_model = False
dnn_lay = N_out_lab_cd
dnn_drop = 0.0
dnn_use_laynorm_inp = False
dnn_use_batchnorm_inp = False
dnn_use_batchnorm = False
dnn_use_laynorm = False
dnn_act = softmax
arch_lr = 0.08
arch_halving_factor = 0.5
arch_improvement_threshold = 0.001
arch_opt = sgd
opt_momentum = 0.0
opt_weight_decay = 0.0
opt_dampening = 0.0
opt_nesterov = False


[architecture4]
arch_name = MLP_soft2
arch_proto = proto/MLP.proto
arch_library = neural_networks
arch_class = MLP
arch_pretrain_file = none
arch_freeze = False
arch_seq_model = False
dnn_lay = 48
dnn_drop = 0.0
dnn_use_laynorm_inp = False
dnn_use_batchnorm_inp = False
dnn_use_batchnorm = False
dnn_use_laynorm = False
dnn_act = softmax
arch_lr = 0.08
arch_halving_factor = 0.5
arch_improvement_threshold = 0.001
arch_opt = sgd
opt_momentum = 0.0
opt_weight_decay = 0.0
opt_dampening = 0.0
opt_nesterov = False


[model]
model_proto = proto/model.proto
model = out_dnn1=compute(CNN_layers,raw)
	out_dnn2=compute(MLP_layers,out_dnn1)
	out_dnn3=compute(MLP_soft1,out_dnn2)
	out_dnn4=compute(MLP_soft2,out_dnn2)
	loss_mono=cost_nll(out_dnn4,lab_mono)
	loss_mono_w=mult_constant(loss_mono,1.0)
	loss_cd=cost_nll(out_dnn3,lab_cd)
	loss_final=sum(loss_cd,loss_mono_w)
	err_final=cost_err(out_dnn3,lab_cd)

[forward]
forward_out = out_dnn3
normalize_posteriors = True
normalize_with_counts_from = lab_cd
save_out_file = False
require_decoding = True

[decoding]
decoding_script_folder = kaldi_decoding_scripts/
decoding_script = decode_dnn.sh
decoding_proto = proto/decoding.proto
min_active = 200
max_active = 7000
max_mem = 50000000
beam = 13.0
latbeam = 8.0
acwt = 0.2
max_arcs = -1
skip_scoring = false
scoring_script = local/score.sh
scoring_opts = "--min-lmwt 1 --max-lmwt 10"
norm_vars = False
