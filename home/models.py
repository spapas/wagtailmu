from django.db import models
from jetstream.fields import FeatureCustomizedStreamField
from jetstream.utils import get_block_tuple
from jetstream.blocks import BaseTwoColumnBlock, COLUMN_PERMITTED_BLOCKS, BaseSidebarLayoutBlock
from wagtail import blocks, fields
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

class TwoColumnBlock(BaseTwoColumnBlock):
    left_column = blocks.StreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-left',
        label='Left column content'
    )

    right_column = blocks.StreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-right',
        label='Right column content'
    )

class SideBarLayoutBlock(BaseSidebarLayoutBlock):
    sidebar = blocks.StreamBlock(
        COLUMN_PERMITTED_BLOCKS,
        icon='arrow-left',
        label='Sidebar content'
    ) 

class HomePage(Page):
    body = fields.StreamField([
        get_block_tuple(TwoColumnBlock()),
        get_block_tuple(SideBarLayoutBlock()),
    ], use_json_field=True)
    
    #body = FeatureCustomizedStreamField([
    #    get_block_tuple(TwoColumnBlock()),
    #    #get_block_tuple(BaseThreeColumnBlock()),
    #    #get_block_tuple(BaseFourColumnBlock()),
    #    # get_block_tuple(BaseSidebarLayoutBlock()),
    #], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]