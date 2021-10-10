from typing import Tuple
from sqlalchemy.orm import relationship
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Enum, Integer, String
from core.models.base_model import Base
from core.models.type_mixin import TypeMixin


class TempMatchEnum(Enum):
    """
    Different temperature comparison cases.

    Ordered by least to most preferable for the yeast instance
    that called can_ferm_with().

    NO_OVERLAP conveniently equates to a falsey value.
    """

    NO_OVERLAP = 0
    EXTREME_OVERLAP = 1
    EXTREME_IDEAL_OVERLAP = 2
    IDEAL_EXTREME_OVERLAP = 3
    IDEAL_OVERLAP = 4
    PERFECT_MATCH = 5

    names = {
        0: "No Overlap - There is no common temperature range for the yeasts to ferment together.",
        1: "Extreme Overlap - Extreem range of yeast one overlaps with extreme range of yeast two.",
        2: "Extreme-Ideal Overlap - Extreme range of yeast one overlaps with ideal range of yeast two.",
        3: "Ideal-Extreme Overlap - Ideal range of yeast one overlaps with extreme range of yeast two.",
        4: "Ideal Overlap - Ideal range of yeast one overlaps with ideal range of yeast two.",
        5: "Perfect Match - Ideal ranges for both tempuratures are the same.",
    }

    @classmethod
    def get_name(cls, member: "TempMatchEnum"):
        return cls.names.get(member)


class Yeast(Base, TypeMixin):
    __tablename__ = "yeasts"
    # name = Column(String(256), nullable=False)
    brand = Column(String(256), nullable=True)
    ideal_low_temp = Column(Integer, nullable=False)
    ideal_high_temp = Column(Integer, nullable=False)
    min_low_temp = Column(Integer, nullable=True)
    max_high_temp = Column(Integer, nullable=True)
    description = Column(String(1024), nullable=True)
    yeast_type_id = Column(Integer, ForeignKey("yeast_types.id"), nullable=False)
    yeast_type = relationship("YeastType", uselist=False)

    def check_temp_match(self, yeast2: "Yeast") -> Tuple[TempMatchEnum, int, int]:
        """
        Determine if this yeast's ideals and extremes allign with another.

        @return: enumeration of match / overlap, min ferm temp, max ferm temp
        """
        min_temp = self.ideal_low_temp
        max_temp = self.ideal_high_temp

        if (
            self.ideal_low_temp == yeast2.ideal_low_temp
            and self.ideal_high_temp == yeast2.ideal_high_temp
        ):
            min_temp = self.ideal_low_temp
            max_temp = self.ideal_high_temp
            return TempMatchEnum.PERFECT_MATCH, min_temp, max_temp

        # we know that at least one of them was not a match
        if (
            self.ideal_low_temp < yeast2.ideal_high_temp
            and self.ideal_high_temp > yeast2.ideal_low_temp
        ):
            min_temp = max(self.ideal_low_temp, yeast2.ideal_low_temp)
            max_temp = min(self.ideal_high_temp, yeast2.ideal_high_temp)
            return TempMatchEnum.IDEAL_OVERLAP, min_temp, max_temp

        # this ideal vs their extremes
        if (
            self.ideal_low_temp < yeast2.max_high_temp
            and self.ideal_high_temp > yeast2.min_low_temp
        ):
            min_temp = max(self.ideal_low_temp, yeast2.min_low_temp)
            max_temp = min(self.ideal_high_temp, yeast2.max_high_temp)
            return TempMatchEnum.IDEAL_EXTREME_OVERLAP, min_temp, max_temp

        # this extremes vs their ideals
        if (
            self.min_low_temp < yeast2.ideal_high_temp
            and self.max_high_temp > yeast2.ideal_low_temp
        ):
            min_temp = max(self.min_low_temp, yeast2.ideal_low_temp)
            max_temp = min(self.max_high_temp, yeast2.ideal_high_temp)
            return TempMatchEnum.EXTREME_IDEAL_OVERLAP, min_temp, max_temp

        # this extremes vs their extremes
        if (
            self.min_low_temp < yeast2.max_high_temp
            and self.max_high_temp > yeast2.min_low_temp
        ):
            min_temp = max(self.min_low_temp, yeast2.min_low_temp)
            max_temp = min(self.max_high_temp, yeast2.max_high_temp)
            return TempMatchEnum.EXTREME_OVERLAP, min_temp, max_temp

        return TempMatchEnum.NO_OVERLAP, min_temp, max_temp


class YeastType(Base, TypeMixin):
    """
    Wet Ale, Wet Lager, Dry Ale, Dry Lager
    TODO: This could be better thought out
    """

    # All we need to define is the table name
    __tablename__ = "yeast_types"
    # TypeMixin handles the name field and the choices() function
