class Party:
    
    def __init__(self):
        self.names = []


party = Party()
while True:
    name = input()

    if name == "End":
        break
    else:
        party.names.append(name)

print(f"Going: {', '.join(party.names)}")
print(f"Total: {len(party.names)}")
