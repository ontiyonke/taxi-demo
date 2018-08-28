from eventsourcing.application.sqlalchemy import SQLAlchemyApplication

from tests.bdd.steps.taxi import TaxiSystem


def before_all(context):
    context.system = TaxiSystem(
        infrastructure_class=SQLAlchemyApplication,
        setup_tables=True,
    )
    context.system.setup()


def after_all(context):
    context.system.close()
