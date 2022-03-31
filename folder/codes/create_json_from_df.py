import json
import pandas as pd
class Json_from_df:
 
    def __init__(self, data_df, save_file):
        self.data_df = data_df
        self.save_file = save_file

    def create_json_from_df(self, data_df, save_file):
        print(data_df)
        corpus_text = data_df.groupby('DocType')["Text"].apply(list).to_json()
        corpus_json = json.loads(corpus_text)

        if save_file:
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(corpus_json, f, ensure_ascii=False, indent=4)

        return corpus_json