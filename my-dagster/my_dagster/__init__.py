# from dagster import Definitions, load_assets_from_modules, op, job

# from . import assets

# defs = Definitions(assets=load_assets_from_modules([assets]))

from dagster import job, op, Definitions


@op
def return_five():
    return 5


@op
def add_one(arg):
    return arg + 1


@job
def do_stuff():
    add_one(return_five())

defs = Definitions(jobs=[do_stuff])
