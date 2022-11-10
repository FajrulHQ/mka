locations = [
    {
        "location": "Arad",
        "to_bucharest": 366,
        "options": [["Zerind", 75], ["Sibiu", 140], ["Timisoara", 118]]
    },
    {
        "location": "Bucharest",
        "to_bucharest": 0,
        "options": [["Pitesti", 101], ["Giurgiu", 90], ["Urziceni", 85], ["Fagaras", 211]]
    },
    {
        "location": "Craiova",
        "to_bucharest": 160,
        "options": [["Pitesti", 138], ["Rimnicu Vilcea", 146], ["Dobreta", 120]]
    },
    {
        "location": "Dobreta",
        "to_bucharest": 242,
        "options": [["Mehadia", 75], ["Craiova", 120]]
    },
    {
        "location": "Eforie",
        "to_bucharest": 161,
        "options": [["Hirsova", 86]]
    },
    {
        "location": "Fagaras",
        "to_bucharest": 178,
        "options": [["Sibiu", 99], ["Bucharest", 211]]
    },
    {
        "location": "Giurgiu",
        "to_bucharest": 77,
        "options": [["Bucharest", 90]]
    },
    {
        "location": "Hirsova",
        "to_bucharest": 151,
        "options": [["Urziceni", 98], ["Eforie", 86]]
    },
    {
        "location": "Iasi",
        "to_bucharest": 226,
        "options": [["Vaslui", 92], ["Neamt", 87]]
    },
    {
        "location": "Lugoj",
        "to_bucharest": 244,
        "options": [["Mehadia", 70], ["Timisoara", 111]]
    },
    {
        "location": "Mehadia",
        "to_bucharest": 241,
        "options": [["Lugoj", 70], ["Dobreta", 75]]
    },
    {
        "location": "Neamt",
        "to_bucharest": 234,
        "options": [["Iasi", 87]]
    },
    {
        "location": "Oradea",
        "to_bucharest": 380,
        "options": [["Zerind", 71], ["Sibiu", 151]]
    },
    {
        "location": "Pitesti",
        "to_bucharest": 98,
        "options": [["Rimnicu Vilcea", 97], ["Bucharest", 101]]
    },
    {
        "location": "Rimnicu Vilcea",
        "to_bucharest": 193,
        "options": [["Sibiu", 80], ["Pitesti", 97]]
    },
    {
        "location": "Sibiu",
        "to_bucharest": 253,
        "options": [["Fagaras", 99], ["Rimnicu Vilcea", 80], ["Arad", 140], ["Oradea", 151]]
    },
    {
        "location": "Timisoara",
        "to_bucharest": 329,
        "options": [["Arad", 118], ["Lugoj", 111]]
    },
    {
        "location": "Urziceni",
        "to_bucharest": 80,
        "options": [["Bucharest", 85], ["Hirsova", 98], ["Vaslui", 142]]
    },
    {
        "location": "Vaslui",
        "to_bucharest": 199,
        "options": [["Iasi", 92], ["Urziceni", 142]]
    },
    {
        "location": "Zerind",
        "to_bucharest": 374,
        "options": [["Oradea", 71], ["Arad", 75]]
    },
]


def get_location(loc):
    return list(filter(lambda x: x["location"] == loc, locations))[0]


def shortest_path(first_loc, method):
    path = [first_loc]
    recent_loc = first_loc
    g_total, i = 0, 0
    # stop when last path in Bucharest
    while path[-1] != "Bucharest" and i < 10:
        location = get_location(recent_loc)
        last_loc = path[-2] if len(path) > 1 else path[-1]
        f = []
        for opt in location["options"]:
            # except calculate on last location
            if opt[0] != last_loc:
                h = get_location(opt[0])["to_bucharest"]
                g = g_total + opt[1]
                if (method == "greedy"):
                    f.append({"location": opt[0], "f(n)": h, "g(n)": opt[1]})
                elif (method == "A*"):
                    f.append({"location": opt[0], "f(n)": h+g, "g(n)": opt[1]})

        min_f = min(f, key=lambda x: x["f(n)"])

        recent_loc = min_f["location"]
        path.append(recent_loc)
        g_total += min_f["g(n)"]
        # i+=1 # to avoid infinite loop
    return " -> ".join(path)
