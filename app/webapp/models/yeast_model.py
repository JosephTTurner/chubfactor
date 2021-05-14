from typing import Tuple
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Enum, Integer, String
from models.base_model import Base


class TempMatchEnum(Enum):
    '''
    Different temperature comparison cases.

    Ordered by least to most preferable for the yeast instance
    that called can_ferm_with().

    NO_OVERLAP conveniently equates to a falsey value.
    '''
    NO_OVERLAP = 0
    EXTREME_OVERLAP = 1
    EXTREME_IDEAL_OVERLAP = 2
    IDEAL_EXTREME_OVERLAP = 3
    IDEAL_OVERLAP = 4
    PERFECT_MATCH = 5


class Yeast(Base):
    __tablename__ = 'yeasts'
    name = Column(String(256), nullable=False)
    brand = Column(String(256), nullable=True)
    ideal_low_temp = Column(Integer, nullable=False)
    ideal_high_temp = Column(Integer, nullable=False)
    min_low_temp = Column(Integer, nullable=True)
    max_high_temp = Column(Integer, nullable=True)
    description = Column(String(1024), nullable=True)
    yeast_type_id = Column(Integer, ForeignKey('yeast_types.id'), nullable=False)
    yeast_type = relationship('YeastType', uselist=False)

    def can_ferm_with(self, yeast2: 'Yeast') -> Tuple[TempMatchEnum, int, int]:
        '''
        Determine if this yeast's ideals and extremes allign with another.

        @return: enumeration of match / overlap, min ferm temp, max ferm temp
        '''
        min_temp = self.ideal_low_temp
        max_temp = self.ideal_high_temp

        if (self.ideal_low_temp == yeast2.ideal_low_temp
        and self.ideal_high_temp == yeast2.ideal_high_temp):
            min_temp = self.ideal_low_temp
            max_temp = self.ideal_high_temp
            return TempMatchEnum.PERFECT_MATCH, min_temp, max_temp

        # we know that at least one of them was not a match
        if (self.ideal_low_temp < yeast2.ideal_high_temp
        and self.ideal_high_temp > yeast2.ideal_low_temp):
            min_temp = max(self.ideal_low_temp, yeast2.ideal_low_temp)
            max_temp = min(self.ideal_high_temp, yeast2.ideal_high_temp)
            return TempMatchEnum.IDEAL_OVERLAP, min_temp, max_temp

        # this ideal vs their extremes
        if (self.ideal_low_temp < yeast2.max_high_temp
        and self.ideal_high_temp > yeast2.min_low_temp):
            min_temp = max(self.ideal_low_temp, yeast2.min_low_temp)
            max_temp = min(self.ideal_high_temp, yeast2.max_high_temp)
            return TempMatchEnum.IDEAL_EXTREME_OVERLAP, min_temp, max_temp

        # this extremes vs their ideals
        if (self.min_low_temp < yeast2.ideal_high_temp
        and self.max_high_temp > yeast2.ideal_low_temp):
            min_temp = max(self.min_low_temp, yeast2.ideal_low_temp)
            max_temp = min(self.max_high_temp, yeast2.ideal_high_temp)
            return TempMatchEnum.EXTREME_IDEAL_OVERLAP, min_temp, max_temp

        # this extremes vs their extremes
        if (self.min_low_temp < yeast2.max_high_temp
        and self.max_high_temp > yeast2.min_low_temp):
            min_temp = max(self.min_low_temp, yeast2.min_low_temp)
            max_temp = min(self.max_high_temp, yeast2.max_high_temp)
            return TempMatchEnum.EXTREME_OVERLAP, min_temp, max_temp

        return TempMatchEnum.NO_OVERLAP, min_temp, max_temp

class YeastType(Base):
    '''
    Wet Ale, Wet Lager, Dry Ale, Dry Lager
    TODO: This could be better thought out
    '''
    __tablename__ = 'yeast_types'
    name = Column(String(256), nullable=False)
