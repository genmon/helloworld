"""empty message

Revision ID: 2f1cc6dd4d08
Revises: 58a3e8869dbb
Create Date: 2013-12-30 16:24:51.715547

"""

# revision identifiers, used by Alembic.
revision = '2f1cc6dd4d08'
down_revision = '58a3e8869dbb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'twitter_friends_cache_twitter_id_friend_twitter_id_key', 'twitter_friends_cache')
    op.create_unique_constraint(None, 'twitter_friends_cache', ['twitter_id', 'friend_twitter_id'])
    op.drop_constraint(u'whoyoulookinat_user_id_looking_at_twitter_display_name_key', 'whoyoulookinat')
    op.create_unique_constraint(None, 'whoyoulookinat', ['user_id', 'looking_at_twitter_display_name'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'whoyoulookinat')
    op.create_unique_constraint(u'whoyoulookinat_user_id_looking_at_twitter_display_name_key', 'whoyoulookinat', [u'looking_at_twitter_display_name', u'user_id'])
    op.drop_constraint(None, 'twitter_friends_cache')
    op.create_unique_constraint(u'twitter_friends_cache_twitter_id_friend_twitter_id_key', 'twitter_friends_cache', [u'friend_twitter_id', u'twitter_id'])
    ### end Alembic commands ###
