# How to recreate the Project

## Create a Virtual Environment
For the virtual environment, I prefer to use **[conda](https://www.anaconda.com/download)**, after installing run the following commands on your terminal one by one, this because you'll be requested to confirm the installations

```bash
conda create -n data_eng python=3.10
conda activate data_eng
# we are going to use dbt to model data in athena and redshift
# in order to make this possible, we will install the required dbt adapter 

python -m pip install dbt-core dbt-redshift dbt-athena

# let us now install terraform (on macos), please refer to the officital docs if you are using a different os
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```
after having everything ready, initiate out terraform project to start building our aws infra.