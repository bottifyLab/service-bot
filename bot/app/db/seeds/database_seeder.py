from orator.seeds import Seeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('subscribes').delete()
        self.db.table('subscribes').insert(
         [ {
            'name': '🍑 Попки в джинсах',
            'description': 'https://bit.ly/demo-content-01',
            'access_body': 'Это видно только после оплаты тарифа',
            'price': 1
          },
          {
            'name': '💦 Девочки твоего двора',
            'description': 'https://bit.ly/demo-content-02',
            'access_body': 'Это видно только после оплаты тарифа',
            'price': 5
          },
          {
            'name': '🍒 Откровенные звезды',
            'description': 'https://bit.ly/demo-content-04',
            'access_body': 'Это видно только после оплаты тарифа',
            'price': 10
          }
        ]
        )

