from datetime import date

from src import db
from src.database.models import Film, Actor


def populate_films():
    harry_potter_and_ph_stone = Film(
        title="Harry Potter and the Philosopher\'s Stone",
        release_date=date(2001, 11, 4),
        description='An orphaned boy enrolls in. school of wizardry, where he Learns the truth about himself, '
                    'his family tansy and the terrible evil that haunts:',
        distributed_by='Warner Bros. Pictures',
        length=152,
        rating=7.6
    )
    harry_potter_and_ch_of_secrets = Film(
        title="Harry Potter and Chamber of Secrets",
        release_date=date(2002, 11, 3),
        description='dsmlklsalkmla:',
        distributed_by='Warner Bros. Pictures',
        length=161,
        rating=7.4
    )
    harry_potter_and_pr_of_azkaban = Film(
        title="Harry Potter and the Prisoner of Azkaban",
        release_date=date(2004, 6, 4),
        description='Aa.dalmlkmksnaksma ,md ,s:',
        distributed_by='Warner Bros. Pictures',
        length=142,
        rating=7.9
    )
    harry_potter_and_goblet_of_fire = Film(
        title="Harry Potter and the Goblet of Fire",
        release_date=date(2005, 11, 6),
        description=',mamazxmxmqlwnksn sm,n;q:',
        distributed_by='Warner Bros. Pictures',
        length=157,
        rating=7.7
    )
    harry_potter_and_order_of_phoenix = Film(
        title="Harry Potter and the Order of Phoenix",
        release_date=date(2007, 7, 19),
        description='vdsmnewam;qlwmlkev:',
        distributed_by='Warner Bros. Pictures',
        length=138,
        rating=7.5
    )
    harry_potter_and_half_of_bl_prince = Film(
        title="Harry Potter and the Half-Blood Prince",
        release_date=date(2009, 7, 16),
        description='sa.,m,nsdvkj,nkjbjvdmbfwnlemrlmlfk,',
        distributed_by='Warner Bros. Pictures',
        length=153,
        rating=7.6
    )
    harry_potter_and_deathly_hallows_pt_1 = Film(
        title="Harry Potter and the Deathly Hallows part 1",
        release_date=date(2010, 11, 18),
        description='Asdaefedvredfredsfcfev:',
        distributed_by='Warner Bros. Pictures',
        length=146,
        rating=7.7
    )
    harry_potter_and_deathly_hallows_pt_2 = Film(
        title="Harry Potter and the Deathly Hallows part 2",
        release_date=date(2011, 7, 13),
        description='ewlkvlknslkdlwemleknlwemlkrnek:',
        distributed_by='Warner Bros. Pictures',
        length=130,
        rating=8.1
    )
    db.session.add(harry_potter_and_ph_stone)
    db.session.add(harry_potter_and_ch_of_secrets)
    db.session.add(harry_potter_and_pr_of_azkaban)
    db.session.add(harry_potter_and_goblet_of_fire)
    db.session.add(harry_potter_and_order_of_phoenix)
    db.session.add(harry_potter_and_half_of_bl_prince)
    db.session.add(harry_potter_and_deathly_hallows_pt_1)
    db.session.add(harry_potter_and_deathly_hallows_pt_2)

    db.session.commit()
    db.session.close()


def populate_actors():
    daniel = Actor(name='Daniel Radcliffe', birthday=date(1989, 7, 23), is_active=True)
    emma_watson = Actor(name='Emma Watson', birthday=date(1990, 4, 15), is_active=True)
    rupert_grint = Actor(name='Rupert Grint', birthday=date(1988, 9, 24), is_active=True)
    richard_harris = Actor(name='Richard Harris', birthday=date(1930, 10, 1), is_active=False)
    michael_gambon = Actor(name='Michael Gambon', birthday=date(1940, 10, 19), is_active=True)
    alan_rickman = Actor(name='Alan Rickman', birthday=date(1946, 2, 21), is_active=False)

    db.session.add(daniel)
    db.session.add(emma_watson)
    db.session.add(rupert_grint)
    db.session.add(richard_harris)
    db.session.add(michael_gambon)
    db.session.add(alan_rickman)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Populating db...')
    populate_films()
    populate_actors()
    print('Successfully populated!')
