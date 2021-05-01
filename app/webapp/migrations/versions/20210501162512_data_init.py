"""data_init

Revision ID: 7e691fd595e3
Revises: 4ef1a479fefd
Create Date: 2021-05-01 16:25:12.717277

"""
from alembic import op
import sqlalchemy as sa
from db_engine import db_session_scope
from webapp.models.color_model import Shade, Color
from webapp.models.brew_model import Brew, Style
from webapp.models.brewer_model import BrewCrew, Brewer, Crew
from webapp.models.chub_factor_model import ChubFactor

# revision identifiers, used by Alembic.
revision = '7e691fd595e3'
down_revision = '4ef1a479fefd'
branch_labels = None
depends_on = None


def upgrade():
    with db_session_scope() as db_session:
        never_not = ChubFactor(name='Never Not', rank=10)
        rock_what_you_got = ChubFactor(name='Rock What You Got', rank=7)
        so_chubby = ChubFactor(name='So Chubby', rank=9)
        db_session.add(never_not)
        db_session.add(rock_what_you_got)
        db_session.add(so_chubby)

        isaac = Brewer(
            nick_name = 'Brewnami',
            chub_factor = never_not
        )
        jerome = Brewer(
            nick_name = 'Brewsydon',
            chub_factor = never_not
        )
        joseph = Brewer(
            nick_name = 'Hoptimus Prime',
            chub_factor = rock_what_you_got
        )
        db_session.add(isaac)
        db_session.add(jerome)
        db_session.add(joseph)

        ju_bros = Crew(
            brewers = [isaac, jerome, joseph],
            name = 'Ju Bros',
            slogan = 'Chub is the is',
            story = 'There we were. So chubby, lesser men would have died. Damned chubby. Now that\'s some shit.',
            chub_factor = so_chubby
        )
        db_session.add(ju_bros)

        dark = Shade(name='Dark')
        medium = Shade(name='Medium')
        chocolate = Color(name='Chocolate')
        red = Color(name='Red')
        db_session.add(dark)
        db_session.add(medium)
        db_session.add(chocolate)
        db_session.add(red)

        stout = Style(
            name = 'Stout',
            shade = dark,
            color = chocolate,
        )
        db_session.add(stout)
        coffeeless_stout = Style(
            name = 'Coffeeless Stout',
            shade = dark,
            color = chocolate,
            parent = stout
        )
        db_session.add(coffeeless_stout)
        irish_red_ale = Style(
            name = 'Irish Red Ale',
            shade = medium,
            color = red,
        )
        db_session.add(irish_red_ale)
        american_red_lager = Style(
            name = 'American Red Lager',
            shade = medium,
            color = red,
            parent = irish_red_ale
        )
        db_session.add(american_red_lager)
        saison = Style(
            name = 'Saison',
            shade = Shade(name='Medium Light'),
            color = Color(name='Gold Orange')
        )
        db_session.add(saison)
        brews = [
            Brew(
                nick_name = 'Last Night of Camp',
                brewer = jerome,
                style = coffeeless_stout,
            ),
            Brew(
                nick_name = 'Sass Dropper',
                brewer = isaac,
                style = saison
            ),
            Brew(
                nick_name = 'Indian Summer',
                brewer = joseph,
                style = american_red_lager,
            )
        ]

        db_session.bulk_save_objects(brews)


def downgrade():
    with db_session_scope() as db_session:
        db_session.query(Style).delete()
        db_session.query(Color).delete()
        db_session.query(Shade).delete()
        db_session.query(Brew).delete()
        db_session.query(Brewer).delete()
        db_session.query(Crew).delete()
        db_session.query(BrewCrew).delete()
        db_session.query(ChubFactor).delete()
