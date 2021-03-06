# Copyright 2018 Alexander Matthews
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch

#pytorch stuff
tdtype = torch.FloatTensor

#Two dimensional plot stuff.
upper_lim = 2.
lower_lim = -1.*upper_lim
points_per_dim = 70

#Hyperparameters.
bias_variance = 0.2
weight_variance = 0.8
noise_variance = 1e-1
shared_depth = 3
hidden_units = 50

#Text for figures
deep_net_name = 'Bayesian deep network'
