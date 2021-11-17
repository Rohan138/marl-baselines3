"""Abstract base classes for MARL algorithms, using vectorized environments."""

import io
import pathlib
import time
from abc import ABC, abstractmethod
from collections import deque
from typing import Any, Dict, Iterable, List, Optional, Tuple, Type, Union

import gym
import numpy as np
import torch as th
from stable_baselines3.common import utils
from stable_baselines3.common.base_class import BaseAlgorithm
from stable_baselines3.common.callbacks import (BaseCallback, CallbackList,
                                                ConvertCallback, EvalCallback)
from stable_baselines3.common.env_util import is_wrapped
from stable_baselines3.common.logger import Logger
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.noise import ActionNoise
from stable_baselines3.common.policies import BasePolicy, get_policy_from_name
from stable_baselines3.common.preprocessing import (
    check_for_nested_spaces, is_image_space, is_image_space_channels_first)
from stable_baselines3.common.save_util import (load_from_zip_file,
                                                recursive_getattr,
                                                recursive_setattr,
                                                save_to_zip_file)
from stable_baselines3.common.type_aliases import (GymEnv, MaybeCallback,
                                                   Schedule)
from stable_baselines3.common.utils import (check_for_correct_spaces,
                                            get_device, get_schedule_fn,
                                            get_system_info, set_random_seed,
                                            update_learning_rate)
from stable_baselines3.common.vec_env import (DummyVecEnv, VecEnv,
                                              VecNormalize, VecTransposeImage,
                                              is_vecenv_wrapped,
                                              unwrap_vec_normalize)


class MultiAgentAlgorithm(BaseAlgorithm):
    def __init__(
        self,
        policy: Type[BasePolicy],
        env: Union[GymEnv, str, None],
        policy_base: Type[BasePolicy],
        learning_rate: Union[float, Schedule],
        policy_kwargs: Optional[Dict[str, Any]] = None,
        tensorboard_log: Optional[str] = None,
        verbose: int = 0,
        device: Union[th.device, str] = "auto",
        support_multi_env: bool = False,
        create_eval_env: bool = False,
        monitor_wrapper: bool = True,
        seed: Optional[int] = None,
        use_sde: bool = False,
        sde_sample_freq: int = -1,
        supported_action_spaces: Optional[Tuple[gym.spaces.Space, ...]] = None,
    ):
        super().__init__(
            policy,
            env,
            policy_base,
            learning_rate,
            policy_kwargs=policy_kwargs,
            tensorboard_log=tensorboard_log,
            verbose=verbose,
            device=device,
            support_multi_env=support_multi_env,
            create_eval_env=create_eval_env,
            monitor_wrapper=monitor_wrapper,
            seed=seed,
            use_sde=use_sde,
            sde_sample_freq=sde_sample_freq,
            supported_action_spaces=supported_action_spaces,
        )
