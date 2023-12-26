import pandas as pd

pr_data = pd.read_excel('F:/test_work/PR_dataset.xlsx')
commits_data = pd.read_excel('F:/test_work/commits_data.xlsx')
commits_changes = pd.read_excel('F:/test_work/commits_changes.xlsx')

merged_data = pd.merge(commits_data, pr_data, how='inner', left_on='pull_request_id', right_on='pull_request_id')

full_data = pd.merge(merged_data, commits_changes, how='inner', left_on='sha', right_on='sha')

pr_additions_sum = full_data.groupby('pull_request_id')['additions'].sum()

large_pr_condition = pr_additions_sum > 500
# Отладочный вывод для значений столбца 'additions'
print("Values of 'additions' column:")
print(full_data[['pull_request_id', 'additions']])
pr_data['is_large_pr'] = large_pr_condition.astype(int)
pr_data['is_large_pr'] = pr_data['is_large_pr'].fillna(0)
pr_data['is_large_pr'] = pr_data['is_large_pr'].astype(int)
print("After conversion:")
print(pr_data[['pull_request_id', 'is_large_pr']])
# Подсчет Large PRs для каждого пользователя
large_prs_by_user = pr_data.groupby('user_id')['is_large_pr'].sum()

# Вывод результатов
# print("Number of Large PRs:", large_pr_condition.sum())
print("Large PRs for each user:")
print(large_prs_by_user)

# # Вывести информацию о "больших" PRs с использованием iterrows
# # Вывести информацию о "больших" PRs с использованием loc
# # Вывести информацию о "больших" PRs с использованием iterrows
# # Преобразовать значения столбца 'is_large_pr' в целые числа с проверкой на NaN
# pr_data['is_large_pr'] = pr_data['is_large_pr'].fillna(0).astype(int)
#
# # Вывести информацию о "больших" PRs с использованием iterrows
# # Вывести информацию о "больших" PRs с использованием iterrows
# # Вывести информацию о "больших" PRs
# # Вывести информацию о "больших" PRs
# # Вывести информацию о "больших" PRs
# print("Information about Large PRs:")
# print(pr_data.loc[large_pr_condition, :])


# num_large_pr = large_pr_condition.sum()
# print("Number of Large PRs:", num_large_pr)
# # print('Information about Large PRs:')
# # print(pr_data[large_pr_condition])
#
# pr_data['is_large_pr'] = pr_data['is_large_pr'].astype(int)
# pr_data['is_large_pr'] = large_pr_condition.astype(int)
# large_prs_by_user = pr_data.groupby('user_id')['is_large_pr'].sum()
#
# print('Large PRs for each user:')
# print(large_prs_by_user)

# large_prs_data = pr_data[pr_data['is_large_pr']]
# print('Information about Large PRs')
# print(large_prs_data)

# selected_users = ['User A', 'User B', 'User C']
#
# selected_users_condition = pr_data['user_id'].isin(selected_users) & large_pr_condition
# selected_large_prs_data = pr_data.loc[selected_users_condition]
# large_prs_by_selected_user = selected_large_prs_data.groupby('user_id')['is_large_pr'].sum()
# print('Large PRs for selected users:')
# print(large_prs_by_selected_user)
