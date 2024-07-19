# %% md
# !pip install torch tensorboard datasets
# %%
from src.utils.experiment_runner import init_experiment
from src.utils.experiment_runner import run_experiment

# Example usage
config_name = 'try1'

# (
#     architectures,
#     pretrain_datasets,
#     finetune_datasets,
#     writer,
# ) = init_experiment(config_name)
experiment_parts = init_experiment(config_name)

# Run the experiment and display the results
results_df = run_experiment(*experiment_parts)

print(results_df)
# %%
print(results_df)
