class CacheConfig:
    @property
    def version(self) -> int: ...
    @version.setter
    def version(self, val: int) -> None: ...
    @property
    def rpt_fcn_enabled(self) -> bool: ...
    @rpt_fcn_enabled.setter
    def rpt_fcn_enabled(self, val: bool) -> None: ...
    @property
    def evictions_enabled(self) -> bool: ...
    @evictions_enabled.setter
    def evictions_enabled(self, val: bool) -> None: ...
    @property
    def set_initial_size(self) -> bool: ...
    @set_initial_size.setter
    def set_initial_size(self, val: bool) -> None: ...
    @property
    def initial_size(self) -> int: ...
    @initial_size.setter
    def initial_size(self, val: int) -> None: ...
    @property
    def min_clean_fraction(self) -> float: ...
    @min_clean_fraction.setter
    def min_clean_fraction(self, val: float) -> None: ...
    @property
    def max_size(self) -> int: ...
    @max_size.setter
    def max_size(self, val: int) -> None: ...
    @property
    def min_size(self) -> int: ...
    @min_size.setter
    def min_size(self, val: int) -> None: ...
    @property
    def epoch_length(self) -> int: ...
    @epoch_length.setter
    def epoch_length(self, val: int) -> None: ...

    #    /* size increase control fields: */
    @property
    def incr_mode(self) -> int: ...
    @incr_mode.setter
    def incr_mode(self, val: int) -> None: ...
    @property
    def lower_hr_threshold(self) -> float: ...
    @lower_hr_threshold.setter
    def lower_hr_threshold(self, val: float) -> None: ...
    @property
    def increment(self) -> float: ...
    @increment.setter
    def increment(self, val: float) -> None: ...
    @property
    def apply_max_increment(self) -> bool: ...
    @apply_max_increment.setter
    def apply_max_increment(self, val: bool) -> None: ...
    @property
    def max_increment(self) -> int: ...
    @max_increment.setter
    def max_increment(self, val: int) -> None: ...
    @property
    def flash_incr_mode(self) -> int: ...
    @flash_incr_mode.setter
    def flash_incr_mode(self, val: int) -> None: ...
    @property
    def flash_multiple(self) -> float: ...
    @flash_multiple.setter
    def flash_multiple(self, val: float) -> None: ...
    @property
    def flash_threshold(self) -> float: ...
    @flash_threshold.setter
    def flash_threshold(self, val: float) -> None: ...

    # /* size decrease control fields: */
    @property
    def decr_mode(self) -> int: ...
    @decr_mode.setter
    def decr_mode(self, val: int) -> None: ...
    @property
    def upper_hr_threshold(self) -> float: ...
    @upper_hr_threshold.setter
    def upper_hr_threshold(self, val: float) -> None: ...
    @property
    def decrements(self) -> float: ...
    @decrements.setter
    def decrements(self, val: float) -> None: ...
    @property
    def apply_max_decrement(self) -> bool: ...
    @apply_max_decrement.setter
    def apply_max_decrement(self, val: bool) -> None: ...
    @property
    def max_decrement(self) -> int: ...
    @max_decrement.setter
    def max_decrement(self, val: int) -> int: ...
    @property
    def epochs_before_eviction(self) -> int: ...
    @epochs_before_eviction.setter
    def epochs_before_eviction(self, val: int) -> None: ...
    @property
    def apply_empty_reserve(self) -> bool: ...
    @apply_empty_reserve.setter
    def apply_empty_reserve(self, val: bool) -> None: ...
    @property
    def empty_reserve(self) -> float: ...
    @empty_reserve.setter
    def empty_reserve(self, val: float) -> None: ...

    # /* parallel configuration fields: */
    @property
    def dirty_bytes_threshold(self) -> int: ...
    @dirty_bytes_threshold.setter
    def dirty_bytes_threshold(self, val: int) -> None: ...
