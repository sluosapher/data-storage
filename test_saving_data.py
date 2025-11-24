# from saving_data import save_lead
from server import save_sales_lead


def main() -> None:
    # run save_lead function in async context
    asyncio.run(save_sales_lead(
        visitor_name="John Doe",
        title="VP of Engineering",
        company="Acme Corp",
        interests_of_solutions="Data storage, backup, high availability",
        interested_in_pilot="yes",
        email="john.doe@example.com",
        phone_number="+1-555-0100",
        next_steps="Schedule follow-up demo next week",
    ))
    print("Mock lead saved to 'sales_leads.xlsx' in sheet 'sales_leads'.")

import asyncio
if __name__ == "__main__":
    main()

