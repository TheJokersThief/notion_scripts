import goodreads_api_client as gr


class BooklistInfo():

    def __init__(self, context):
        self.client = context.obj['client']
        self.config = context.obj['config'].get('booklist_info')
        self.gr_client = gr.Client(developer_key=self.config.get('goodreads_api_token'))

        table_data = self._get_db_data()
        self._process_table_data(table_data)

    def _get_db_data(self):
        cv = self.client.get_collection_view(self.config.get('page'))
        return cv.collection.get_rows(search="Penguin")

    def _process_table_data(self, data):
        for row in data:
            if row.do_not_process:
                print(f"Not processing {row.title}")
                continue
            print(f"Now processing {row.title}")

            book = self.gr_client.Book.title(row.title)  # pylint: disable=no-member
            print(f"Got book info for goodreads book {book.get('title')}")
            if book:
                for column, api_field in self.config.get('columns').items():
                    coltype = type(getattr(row, column)) if getattr(row, column) is not None else str
                    raw_value = book.get(api_field)
                    if raw_value:
                        # Cast the value to the appropriate type
                        value = coltype(raw_value)
                        setattr(row, column, value)

            row.do_not_process = True
