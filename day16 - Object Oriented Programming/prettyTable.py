from prettytable import PrettyTable

# create a table
table = PrettyTable();

# add column with its data
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]);
table.add_column("Type", ["Electric", "Water", "Earth"]);

# change the align of the table
table.align = "r";

# show the tables
print(table);
