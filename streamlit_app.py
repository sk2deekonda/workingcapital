def working_capital_management():
    # Inputs
    cost_per_unit = float(input("Enter the cost to manufacture one unit of the product (INR): "))
    selling_price_per_unit = float(input("Enter the selling price of one unit of the product (INR): "))
    units_to_sell = int(input("Enter the number of units you plan to sell: "))
    turnaround_time = int(input("Enter the turnaround time to manufacture the product (in days): "))
    payout_time = int(input("Enter the payout time (time to receive payment from customers in days): "))
    daily_operational_costs = float(input("Enter your daily operational costs (INR): "))
    safety_margin = float(input("Enter the safety margin you want to maintain (as a percentage, e.g., 20 for 20%): ")) / 100

    # Calculations
    total_manufacturing_cost = cost_per_unit * units_to_sell
    total_revenue = selling_price_per_unit * units_to_sell
    gross_profit = total_revenue - total_manufacturing_cost

    # Working Capital Requirements
    # Initial investment should cover manufacturing costs and operational costs during the turnaround time
    initial_investment = total_manufacturing_cost + (daily_operational_costs * turnaround_time)

    # Amount to keep in hand should cover operational costs during the payout time plus a safety margin
    amount_to_keep_in_hand = (daily_operational_costs * payout_time) * (1 + safety_margin)

    # Output
    print("\n--- Working Capital Management Results ---")
    print(f"Total Manufacturing Cost: INR {total_manufacturing_cost:,.2f}")
    print(f"Total Revenue: INR {total_revenue:,.2f}")
    print(f"Gross Profit: INR {gross_profit:,.2f}")
    print(f"Initial Investment Required: INR {initial_investment:,.2f}")
    print(f"Amount to Keep in Hand: INR {amount_to_keep_in_hand:,.2f}")

# Run the function
working_capital_management()
