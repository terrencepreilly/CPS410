import unittest
from test_abstracts import (  # noqa: F401
    RenderedBaseTestCase,
    ActorBaseTestCase,
    )
from test_ships import (  # noqa: F401
    EnemyTestCase,
    PlayerTestCase,
    PlayerEnemyInteractionTestCase,
    )

if __name__ == '__main__':
    unittest.main()
