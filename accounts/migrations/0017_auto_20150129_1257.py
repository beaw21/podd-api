# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20150129_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(default=b'', max_length=100, verbose_name='\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e1c\u0e39\u0e49\u0e43\u0e0a\u0e49', blank=True, choices=[(b'', b''), (b'VOLUNTEER', '\u0e2d\u0e32\u0e2a\u0e32\u0e2a\u0e21\u0e31\u0e04\u0e23\u0e42\u0e04\u0e23\u0e07\u0e01\u0e32\u0e23'), (b'ADDITION_VOLUNTEER', '\u0e2d\u0e32\u0e2a\u0e32\u0e2a\u0e21\u0e31\u0e04\u0e23\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e40\u0e15\u0e34\u0e21'), (b'COORDINATOR', '\u0e1c\u0e39\u0e49\u0e1b\u0e23\u0e30\u0e2a\u0e32\u0e19\u0e07\u0e32\u0e19')]),
            preserve_default=True,
        ),
    ]
