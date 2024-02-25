from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)


# Define a route and a function to handle the request
@app.route('/api/entry', methods=['GET'])
def get_entry_items():
    # Replace this with your actual list of items
    items = ['item1', 'item2', 'item3']
    return jsonify(
        {
            "saveEntry": [
                {
                    "id": 1,
                    "Name": "John Doe",
                    "Position": "Software Engineer",
                    "EntryTime": "2024-02-25T12:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 2,
                    "Name": "Jane Smith",
                    "Position": "Data Scientist",
                    "EntryTime": "2024-02-25T09:15:00",
                    "EntryStatus": 0
                },
                {
                    "id": 3,
                    "Name": "Michael Johnson",
                    "Position": "Network Engineer",
                    "EntryTime": "2024-02-25T11:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 4,
                    "Name": "Emily Davis",
                    "Position": "UI/UX Designer",
                    "EntryTime": "2024-02-25T14:45:00",
                    "EntryStatus": 0
                },
                {
                    "id": 5,
                    "Name": "Alex Brown",
                    "Position": "System Analyst",
                    "EntryTime": "2024-02-25T10:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 6,
                    "Name": "Eva Wilson",
                    "Position": "Product Manager",
                    "EntryTime": "2024-02-25T13:20:00",
                    "EntryStatus": 0
                },
                {
                    "id": 7,
                    "Name": "David Johnson",
                    "Position": "DevOps Engineer",
                    "EntryTime": "2024-02-25T08:45:00",
                    "EntryStatus": 1
                },
                {
                    "id": 8,
                    "Name": "Sophie Miller",
                    "Position": "Marketing Specialist",
                    "EntryTime": "2024-02-25T15:00:00",
                    "EntryStatus": 0
                },
                {
                    "id": 9,
                    "Name": "Ryan Davis",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T09:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 10,
                    "Name": "Olivia White",
                    "Position": "UX Designer",
                    "EntryTime": "2024-02-25T11:45:00",
                    "EntryStatus": 0
                },
                {
                    "id": 11,
                    "Name": "Mia Brown",
                    "Position": "Software Engineer",
                    "EntryTime": "2024-02-25T14:15:00",
                    "EntryStatus": 1
                },
                {
                    "id": 12,
                    "Name": "Nathan Johnson",
                    "Position": "Data Scientist",
                    "EntryTime": "2024-02-25T08:00:00",
                    "EntryStatus": 0
                },
                {
                    "id": 13,
                    "Name": "Emma Wilson",
                    "Position": "Product Manager",
                    "EntryTime": "2024-02-25T12:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 14,
                    "Name": "Matthew White",
                    "Position": "Network Engineer",
                    "EntryTime": "2024-02-25T10:45:00",
                    "EntryStatus": 0
                },
                {
                    "id": 15,
                    "Name": "Thanbanoor Shantha",
                    "Position": "UI/UX Designer",
                    "EntryTime": "2024-02-25T13:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 16,
                    "Name": "James Davis",
                    "Position": "System Analyst",
                    "EntryTime": "2024-02-25T09:15:00",
                    "EntryStatus": 0
                },
                {
                    "id": 17,
                    "Name": "Chloe Wilson",
                    "Position": "DevOps Engineer",
                    "EntryTime": "2024-02-25T11:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 18,
                    "Name": "Daniel Brown",
                    "Position": "Marketing Specialist",
                    "EntryTime": "2024-02-25T14:45:00",
                    "EntryStatus": 0
                },
                {
                    "id": 19,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 20,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 21,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 22,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 23,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 24,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 25,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 26,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 27,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 28,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 29,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 30,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 31,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 32,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 33,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 34,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 35,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 36,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 37,
                    "Name": "Grace Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T10:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 101,
                    "Name": "Isaac Wilson",
                    "Position": "Software Engineer",
                    "EntryTime": "2024-02-25T12:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 101,
                    "Name": "Isaac Wilson",
                    "Position": "Software Engineer",
                    "EntryTime": "2024-02-25T12:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 102,
                    "Name": "Isaac Wilson",
                    "Position": "Software Engineer",
                    "EntryTime": "2024-02-25T12:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 103,
                    "Name": "Isaac Wilson",
                    "Position": "Software Engineer",
                    "EntryTime": "2024-02-25T12:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 111,
                    "Name": "Lily Davis",
                    "Position": "Data Scientist",
                    "EntryTime": "2024-02-25T09:15:00",
                    "EntryStatus": 0
                },
                {
                    "id": 222,
                    "Name": "Logan Johnson",
                    "Position": "Product Manager",
                    "EntryTime": "2024-02-25T11:00:00",
                    "EntryStatus": 1
                },
                {
                    "id": 333,
                    "Name": "Zoe White",
                    "Position": "UX Designer",
                    "EntryTime": "2024-02-25T14:45:00",
                    "EntryStatus": 0
                },
                {
                    "id": 444,
                    "Name": "Aiden Wilson",
                    "Position": "System Analyst",
                    "EntryTime": "2024-02-25T10:30:00",
                    "EntryStatus": 1
                },
                {
                    "id": 555,
                    "Name": "Aria Miller",
                    "Position": "Product Manager",
                    "EntryTime": "2024-02-25T13:20:00",
                    "EntryStatus": 0
                },
                {
                    "id": 666,
                    "Name": "Carter Johnson",
                    "Position": "DevOps Engineer",
                    "EntryTime": "2024-02-25T08:45:00",
                    "EntryStatus": 1
                },
                {
                    "id": 777,
                    "Name": "Hannah Davis",
                    "Position": "Marketing Specialist",
                    "EntryTime": "2024-02-25T15:00:00",
                    "EntryStatus": 0
                },
                {
                    "id": 554,
                    "Name": "Elijah Johnson",
                    "Position": "Business Analyst",
                    "EntryTime": "2024-02-25T09:30:00",
                    "EntryStatus": 1
                }
            ]
        }

    )


# @app.route('/api/exit', methods=['GET'])
# def get_exit_items():
#     # Replace this with your actual list of items
#      = ['item1', 'item2', 'item3']
#     return jsonify(
#         {
#             "saveEntry": [
#                 {
#                     "Name": "John Doe",
#                     "id": 1,
#                     "Position": "Software Engineer",
#                     "EntryTime": "2024-02-25T12:30:00"
#                 },
#                 {
#                     "Name": "Jane Smith",
#                     "id": 2,
#                     "Position": "Data Scientist",
#                     "EntryTime": "2024-02-25T09:15:00"
#                 },
#                 {
#                     "Name": "Bob Johnson",
#                     "id": 3,
#                     "Position": "UX Designer",
#                     "EntryTime": "2024-02-25T08:00:00"
#                 }
#
#             ]
#         }
#
#     )


# Run the application
if __name__ == '__main__':
    app.run(port=8001)
