from orator.migrations import Migration


class CreateTicketsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('tickets') as table:
            table.increments('id')
            table.string('code').unique(True)
            table.float('amount')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('tickets')
