import shelve
from shelve import Shelf


class DictStore:
    def __init__(self, filename: str):
        """
        DB SCHEMA:
        row_id(int | str) : row(dict | ...)
        """
        self.db: Shelf = shelve.open(filename)

    def __str__(self) -> str:
        string_rows = ""
        for user_id, row in self.db.items():
            string_rows += f"{user_id}: {str(row)}\n"
        return string_rows

    def __len__(self) -> int:
        return len(self.db.items())

    def create(self, row_id: str, **payload):
        if row_id not in self.db:
            self.db[row_id] = payload
        else:
            self.update(row_id, **payload)

    def update(self, row_id: str, **payload):
        store = self.db[row_id]
        store.update(payload)
        self.db[row_id] = store

    def drop(self, row_id: str):
        del self.db[row_id]

    def count_ids(self) -> dict:
        buff_dict = {}
        for value in self.db.values():

            if current_id := value.get("approach_id", None):

                if buff_dict.get(current_id, None) is None:
                    buff_dict[current_id] = 1
                else:
                    buff_dict[current_id] += 1

        return buff_dict
