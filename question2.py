# Create two separate lists for Catholic and Anglican martyrs.
catholic_martyrs = [
    "Achileo Kiwanuka", "Adolphus Ludigo-Mukasa", "Ambrosius Kibuuka", "Anatoli Kiriggwajjo",
    "Andrew Kaggwa", "Antanansio Bazzekuketta", "Bruno Sserunkuuma", "Charles Lwanga",
    "Denis Ssebuggwawo Wasswa", "Gonzaga Gonza", "Gyavira Musoke", "Yowana Mukiibi",
    "Yusufu Lugalama", "Zakayo Lubega", "James Buuzaabalyaawo", "John Maria Muzeeyi",
    "Joseph Mukasa Kizito", "Lukka Baanabakintu", "Matiya Mulumba", "Mbaga Tuzinde",
    "Mugagga Lubowa", "Mukasa Kiriwawanvu", "Nowa Mawaggali", "Ponsiano Ngondwe"
]

anglican_martyrs = [
    "Aaron Lubega", "Apollo Kivebulaya", "Eria Sebukyala", "Fredrick Kizza", "George Kizza",
    "James Hannington", "Janani Luwum", "Joseph Balikuddembe", "Kizito",
    "Mark Kakumba", "Matia Mulumba", "Nuhu Mbegu", "Robert Munyagayirwa", "Samwiri Mukasa",
    "Yefusa Namayanja", "Yohana Mukasa", "Yosefu Lugalama", "Yowana Kitaka", "Yowana Maria Mukasa"
]

# Remove duplicate names that are present in both lists.
catholic_martyrs = list(set(catholic_martyrs) - set(anglican_martyrs))

# Define a function to determine the group of the martyr.
def martyr_count(name):
    if name in catholic_martyrs:
        return "Catholic"
    elif name in anglican_martyrs:
        return "Anglican"
    else:
        return "Not Found"

# Determine the group of the martyr named "Kizito".
kizito_group = martyr_count("Kizito")

# Function to check if a given string matches any of the martyr names in both lists.
def is_martyr_name(name):
    return name in catholic_martyrs or name in anglican_martyrs

# Example usage of the function:
input_name = "Mugagga Lubowa"
result = is_martyr_name(input_name)
print(result)