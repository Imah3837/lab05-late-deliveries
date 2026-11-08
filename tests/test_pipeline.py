from latedeliveries.data import make_orders


def test_data_created():

    df = make_orders()

    assert len(df) > 0


def test_target_exists():

    df = make_orders()

    assert "late" in df.columns


def test_distance_exists():

    df = make_orders()

    assert "distance_km" in df.columns