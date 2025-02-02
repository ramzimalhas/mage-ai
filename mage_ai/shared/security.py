import os

MIN_SECRET_ENV_VAR_LENGTH = 8
WHITELISTED_ENV_VARS = set([
    'MAGE_REPO_PATH',
    'HOME',
    'PWD',
])


def filter_out_env_var_values(value: str):
    env_var_values = dict(os.environ).values()
    env_var_values = [v for v in env_var_values
                      if v and len(v) >= MIN_SECRET_ENV_VAR_LENGTH
                      and v not in WHITELISTED_ENV_VARS]
    env_var_values.sort(key=len, reverse=True)
    value_clean = value
    for env_var_value in env_var_values:
        replace_value = '*' * len(env_var_value)
        value_clean = value_clean.replace(env_var_value, replace_value)
    return value_clean
