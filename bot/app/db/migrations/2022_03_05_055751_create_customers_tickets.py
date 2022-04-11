from orator.migrations import Migration


class CreateCustomersTickets(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('customers_tickets') as table:
            table.increments('id')
            table.integer('ticket_id').unsigned()
            table.integer('customer_id').unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('customers_tickets')
