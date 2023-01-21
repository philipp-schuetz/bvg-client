from query import Query
from rich.console import Console
from rich.table import Table

# station_query = input('provide station name: ')
console = Console()



query = Query()
stops = query.get_stops('Edelweiß')


table = Table(show_header=True, header_style='bold blue')
table.add_column('ID', style='dim', width=16)
table.add_column('Name', min_width=16)

for stop in stops:
    table.add_row(stop['id'], stop['name'])


console.print(table)