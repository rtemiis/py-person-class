class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    result_list = []

    for person in people_data:
        Person.people[person.get("name")] = Person(
            person.get("name"),
            person.get("age")
        )

    for person in people_data:
        name = person.get("name")
        if person.get("wife") and person.get("wife") is not None:
            spouse_name = person.get("wife")
            Person.people[name].wife = Person.people[spouse_name]
        elif person.get("husband") and person.get("husband") is not None:
            spouse_name = person.get("husband")
            Person.people[name].husband = Person.people[spouse_name]
        result_list.append(Person.people[name])

    return result_list
