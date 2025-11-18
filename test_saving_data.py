from saving_data import save_lead


def main() -> None:
    save_lead(
        visitor_name="John Doe",
        title="VP of Engineering",
        company="Acme Corp",
        interests_of_solutions="Data storage, backup, high availability",
        interested_in_pilot="yes",
        email="john.doe@example.com",
        phone_number="+1-555-0100",
        next_steps="Schedule follow-up demo next week",
    )
    print("Mock lead saved to 'sales_leads.xlsx' in sheet 'sales_leads'.")


if __name__ == "__main__":
    main()

