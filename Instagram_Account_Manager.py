import json

class UserData:
    def __init__(self):
        self.filename = "Instagram_Account's.json"

    def get_user_details(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        number = input("Enter your phone number: ")
        return {"email": email, "password": password, "number": number}

    def save_user_details(self, details):
        all_details = self.load_all_user_details()
        details['id'] = len(all_details) + 1
        all_details.append(details)
        with open(self.filename, "w") as file:
            json.dump(all_details, file)
        print("User details saved successfully.")

    def load_all_user_details(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def update_user_details(self, user_id, new_details):
        all_details = self.load_all_user_details()
        for detail in all_details:
            if detail['id'] == user_id:
                detail.update(new_details)
                with open(self.filename, "w") as file:
                    json.dump(all_details, file)
                print("User details updated successfully.")
                return
        print("User ID not found.")

    def delete_user_details(self, user_id):
        all_details = self.load_all_user_details()
        all_details = [detail for detail in all_details if detail['id'] != user_id]
        with open(self.filename, "w") as file:
            json.dump(all_details, file)
        print("User details deleted successfully.")

class UserInterface:
    def __init__(self):
        self.user_data = UserData()

    def display_user_details(self, details):
        for detail in details:
            print(f"ID: {detail['id']}, Email: {detail['email']}, Password: {detail['password']}, Number: {detail['number']}")

    def run(self):
        while True:
            print("\n1. Save User Details")
            print("\n2. View User Details")
            print("\n3. Edit User Details")
            print("\n4. Delete User Details")
            print("\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                details = self.user_data.get_user_details()
                self.user_data.save_user_details(details)
            elif choice == '2':
                all_details = self.user_data.load_all_user_details()
                if all_details:
                    self.display_user_details(all_details)
                else:
                    print("No existing user details found.")
            elif choice == '3':
                user_id = int(input("Enter the user ID to edit: "))
                new_details = self.user_data.get_user_details()
                self.user_data.update_user_details(user_id, new_details)
            elif choice == '4':
                user_id = int(input("Enter the user ID to delete: "))
                self.user_data.delete_user_details(user_id)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
