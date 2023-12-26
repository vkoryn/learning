import pandas as pd

pr_data = pd.read_excel('F:/test_work/PR_dataset.xlsx')
commits_data = pd.read_excel('F:/test_work/commits_data.xlsx')
commits_changes = pd.read_excel('F:/test_work/commits_changes.xlsx')

merged_data = pd.merge(commits_data, pr_data, how='inner', left_on='pull_request_id', right_on='pull_request_id')

full_data = pd.merge(merged_data, commits_changes, how='inner', left_on='sha', right_on='sha')

# Сначала создайте DataFrame с суммарными добавлениями для каждого pull_request_id
pr_additions_sum = full_data.groupby('pull_request_id')['additions'].sum().reset_index()

# Создайте столбец is_large_pr на основе условия
pr_additions_sum['is_large_pr'] = (pr_additions_sum['additions'] > 500).astype(int)

# Объедините pr_data с pr_additions_sum по pull_request_id
pr_data = pd.merge(pr_data, pr_additions_sum[['pull_request_id', 'is_large_pr']], how='left', on='pull_request_id')

# Подсчет Large PRs для каждого пользователя
large_prs_by_user = pr_data.groupby('user_id')['is_large_pr'].sum()

# Вывод результатов
# print("Number of Large PRs:", pr_additions_sum['is_large_pr'].sum())
# print("Large PRs for each user:")
# print(large_prs_by_user)


# Подсчет Large PRs для каждого пользователя
large_prs_by_user = pr_data.groupby('user_id')['is_large_pr'].sum()

# Создаем DataFrame с информацией о Large PRs для каждого пользователя
result_df = pd.DataFrame({
    'user_id': large_prs_by_user.index,
    'large_pr_count': large_prs_by_user.values
})

# Вывод результатов
print("Large PRs for each user:")
print(result_df)
# Этот код создаст DataFrame result_df, который содержит информацию о количестве Large PRs для каждого пользователя. Вывод будет более структурированным и легко читаемым.