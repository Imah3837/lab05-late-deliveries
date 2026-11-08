from latedeliveries.evaluation import order_cost


def test_cost_function():

    y_true = [1, 1, 0, 0]
    flagged = [1, 0, 1, 0]

    result = order_cost(
        y_true,
        flagged,
    )

    assert result == 23