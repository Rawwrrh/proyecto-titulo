# Generated by Django 3.2.3 on 2021-11-30 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('cod_articulo', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, default='', max_length=120)),
            ],
            options={
                'verbose_name': 'Articulo',
                'db_table': 'ARTICULO',
            },
        ),
        migrations.CreateModel(
            name='Bulto',
            fields=[
                ('id_bulto', models.AutoField(primary_key=True, serialize=False)),
                ('orden_venta', models.CharField(max_length=40)),
                ('tipo_bulto', models.CharField(max_length=80)),
                ('largo', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ancho', models.DecimalField(decimal_places=5, max_digits=10)),
                ('alto', models.DecimalField(decimal_places=5, max_digits=10)),
                ('volumen', models.DecimalField(decimal_places=5, max_digits=10)),
                ('peso_bruto', models.DecimalField(decimal_places=5, max_digits=10)),
                ('peso_neto', models.DecimalField(decimal_places=5, max_digits=10)),
                ('activo', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Bulto',
                'db_table': 'BULTO',
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id_cita', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_cita', models.DateField()),
                ('hora_cita', models.CharField(max_length=10)),
                ('operador_logistico', models.CharField(max_length=120)),
                ('cliente', models.CharField(max_length=120)),
                ('activo', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cita',
                'db_table': 'CITA',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, default='', max_length=70)),
                ('direccion', models.CharField(blank=True, default='', max_length=120)),
                ('telefono', models.CharField(blank=True, default='', max_length=50)),
                ('nom_contacto', models.CharField(blank=True, default='', max_length=50)),
                ('correo_contacto', models.CharField(blank=True, default='', max_length=60)),
            ],
            options={
                'verbose_name': 'Cliente',
                'db_table': 'CLIENTE',
            },
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id_despacho', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, default='', max_length=100)),
                ('comuna', models.CharField(blank=True, default='', max_length=80)),
                ('guia_despacho', models.CharField(blank=True, default=None, max_length=50)),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Despacho',
                'db_table': 'DESPACHO',
            },
        ),
        migrations.CreateModel(
            name='IndicadorDespacho',
            fields=[
                ('id_int_dep', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_despacho', models.CharField(blank=True, max_length=100)),
                ('cantidad_despacho', models.IntegerField()),
                ('exitos', models.IntegerField()),
                ('estado_final', models.IntegerField()),
                ('fecha', models.DateField()),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Indicador_Despacho',
                'db_table': 'INDICADOR_DESPACHO',
            },
        ),
        migrations.CreateModel(
            name='IndicadorTipoVenta',
            fields=[
                ('id_int_tp', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_venta', models.CharField(blank=True, max_length=100)),
                ('cantidad_despacho', models.IntegerField()),
                ('exitos', models.IntegerField()),
                ('estado_final', models.IntegerField()),
                ('fecha', models.DateField(auto_now=True)),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Indicador_Tipo_Venta',
                'db_table': 'INDICADOR_TIPO_VENTA',
            },
        ),
        migrations.CreateModel(
            name='LineaEmbalaje',
            fields=[
                ('cod_le', models.AutoField(primary_key=True, serialize=False)),
                ('orden_venta', models.CharField(max_length=20)),
                ('cod_articulo', models.CharField(max_length=30)),
                ('linea', models.IntegerField()),
                ('descripcion_articulo', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Linea_Embalaje',
                'db_table': 'LINEA_EMBALAJE',
            },
        ),
        migrations.CreateModel(
            name='LineaNoLiberada',
            fields=[
                ('cod_lnl', models.AutoField(primary_key=True, serialize=False)),
                ('orden_venta', models.CharField(max_length=20)),
                ('cod_articulo', models.CharField(max_length=30)),
                ('linea', models.IntegerField()),
                ('descripcion_articulo', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Linea_No_Liberada',
                'db_table': 'LINEA_NO_LIBERADA',
            },
        ),
        migrations.CreateModel(
            name='LineaPicking',
            fields=[
                ('cod_lp', models.AutoField(primary_key=True, serialize=False)),
                ('orden_venta', models.CharField(max_length=20)),
                ('cod_articulo', models.CharField(max_length=30)),
                ('linea', models.IntegerField()),
                ('descripcion_articulo', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Linea_Picking',
                'db_table': 'LINEA_PICKING',
            },
        ),
        migrations.CreateModel(
            name='LineaReparto',
            fields=[
                ('cod_lr', models.AutoField(primary_key=True, serialize=False)),
                ('orden_venta', models.CharField(max_length=20)),
                ('cod_articulo', models.CharField(max_length=30)),
                ('linea', models.IntegerField()),
                ('descripcion_articulo', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField()),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Linea_Reparto',
                'db_table': 'LINEA_REPARTO',
            },
        ),
        migrations.CreateModel(
            name='OrdenVenta',
            fields=[
                ('orden_venta', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('tipo_pago', models.CharField(max_length=30, verbose_name='Tipo de pago')),
                ('canal_venta', models.CharField(max_length=20)),
                ('orden_compra', models.CharField(max_length=50)),
                ('tipo_venta', models.CharField(max_length=30, verbose_name='Tipo de venta')),
                ('tipo_despacho', models.CharField(blank=True, default='', max_length=50, verbose_name='Tipo de venta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.cliente')),
            ],
            options={
                'verbose_name': 'OrdenVenta',
                'db_table': 'ORDEN_VENTA',
            },
        ),
        migrations.CreateModel(
            name='Retiro',
            fields=[
                ('id_retiro', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.CharField(max_length=10)),
                ('hora_fin', models.CharField(max_length=10)),
                ('cliente', models.CharField(max_length=120)),
                ('direccion', models.CharField(max_length=120)),
                ('activo', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Retiro',
                'db_table': 'RETIRO',
            },
        ),
        migrations.CreateModel(
            name='TemporalLinea',
            fields=[
                ('id_linea', models.AutoField(primary_key=True, serialize=False)),
                ('num_linea', models.IntegerField()),
                ('orden_venta', models.CharField(blank='', max_length=40)),
            ],
            options={
                'verbose_name': 'Temp_Linea',
                'db_table': 'TMP_LINEA',
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id_transporte', models.AutoField(primary_key=True, serialize=False)),
                ('ot', models.CharField(blank=True, default='', max_length=20)),
                ('empresa', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Transporte',
                'db_table': 'TRANSPORTE',
            },
        ),
        migrations.CreateModel(
            name='Planificacion',
            fields=[
                ('id_planificacion', models.AutoField(primary_key=True, serialize=False)),
                ('llave_busqueda', models.CharField(blank=True, max_length=30)),
                ('fecha_planificacion', models.DateField()),
                ('orden_venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.ordenventa')),
            ],
            options={
                'verbose_name': 'Planificacion',
                'db_table': 'PLANIFICACION',
            },
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id_linea', models.AutoField(primary_key=True, serialize=False)),
                ('num_linea', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('estado', models.CharField(max_length=40)),
                ('valor', models.IntegerField()),
                ('activo', models.BooleanField(default=False)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.articulo')),
                ('despacho', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.despacho')),
                ('orden_venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.ordenventa')),
            ],
            options={
                'verbose_name': 'Linea',
                'db_table': 'LINEA',
            },
        ),
        migrations.CreateModel(
            name='DetalleRetiro',
            fields=[
                ('id_detalle_retiro', models.AutoField(primary_key=True, serialize=False)),
                ('orden_venta', models.CharField(max_length=40)),
                ('linea', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('tipo_embalaje', models.CharField(max_length=120)),
                ('activo', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('retiro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.retiro')),
            ],
            options={
                'verbose_name': 'Detalle_Retiro',
                'db_table': 'DETALLE_Retiro',
            },
        ),
        migrations.CreateModel(
            name='DetalleCita',
            fields=[
                ('id_detalle_cita', models.AutoField(primary_key=True, serialize=False)),
                ('orden_venta', models.CharField(max_length=40)),
                ('linea', models.CharField(max_length=40)),
                ('codigo_articulo', models.CharField(max_length=80)),
                ('descripcion', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('tipo_embalaje', models.CharField(max_length=120)),
                ('activo', models.BooleanField(default=False)),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.cita')),
            ],
            options={
                'verbose_name': 'Detalle_Cita',
                'db_table': 'DETALLE_CITA',
            },
        ),
        migrations.CreateModel(
            name='DetalleBulto',
            fields=[
                ('id_detalle_bulto', models.AutoField(primary_key=True, serialize=False)),
                ('linea', models.CharField(max_length=10)),
                ('codigo', models.CharField(max_length=60)),
                ('articulo', models.CharField(max_length=120)),
                ('cantidad', models.IntegerField()),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('activo', models.BooleanField(default=False)),
                ('bulto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.bulto')),
            ],
            options={
                'verbose_name': 'Detalle_Bulto',
                'db_table': 'DETALLE_BULTO',
            },
        ),
        migrations.AddField(
            model_name='despacho',
            name='transporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control_procesos_logisticos.transporte'),
        ),
    ]
