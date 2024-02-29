import matplotlib.pyplot as plt


from src.dbrepo.dict_store import DictStore


def approach_text(approach_dict: dict) -> str:
    txt_buffer = ""
    for k, v in approach_dict.items():
        txt_buffer += f"{k}. {v}\n\n"
    return txt_buffer


def create_plot_picture(db: DictStore, decode_dict: dict, filename: str) -> dict:
    approachs_counter = db.count_ids()
    labels = [decode_dict[key] for key in approachs_counter]
    sizes = [approachs_counter[key] for key in approachs_counter]
    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.axis("equal")
    plt.title("Результат")
    plt.legend(loc="upper right")
    plt.savefig(filename, bbox_inches="tight")
    plt.close()
    return {decode_dict[key]: approachs_counter[key] for key in approachs_counter}
