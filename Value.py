# Calculate average transaction value based on total revenue and number of transactions
def calculate_average_transaction_value(total_revenue, num_transactions):
    return total_revenue / num_transactions if num_transactions > 0 else 0

# Example usage:
total_revenue = 10000  # Total revenue
num_transactions = 50  # Number of transactions
average_transaction_value = calculate_average_transaction_value(total_revenue, num_transactions)
print("Average transaction value:", average_transaction_value)
