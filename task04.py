car = {"brand": ["Chevrolet"],
        "model": "Cobalt",
        "color": "white"        
}
car = {"brand": "Chevrolet",
        "model": "Cobalt",
        "color": ["white"],
}
a = car ["brand"]
b = car ["color"]

print(a,b)