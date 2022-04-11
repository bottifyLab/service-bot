from orator.migrations import Migration


class CreatePaymentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('payments') as table:
            table.integer('customer_id').unsigned()
            table.foreign('customer_id').references('id').on('customers').on_delete('cascade')
            table.increments('id')
            table.float('amount')
            table.string('comment')
            table.string('provider')
            table.boolean('confirmed').default(False)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('payments')
