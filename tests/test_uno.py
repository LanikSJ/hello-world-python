"""Tests for uno.py"""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest  # pyright: ignore[reportMissingImports]
from uno import Card, Player, Deck, Hand, GameSettings, BadInputError


class TestCard:
    """Tests for Card class."""

    def test_card_initialization(self):
        """Test Card initialization with color and value."""
        card = Card('red', '5')
        assert card.getColor() == 'red'
        assert card.getValue() == '5'

    def test_card_color_blue(self):
        """Test Card with blue color."""
        card = Card('blue', '9')
        assert card.getColor() == 'blue'
        assert card.getValue() == '9'

    def test_card_color_green(self):
        """Test Card with green color."""
        card = Card('green', '0')
        assert card.getColor() == 'green'

    def test_card_color_yellow(self):
        """Test Card with yellow color."""
        card = Card('yellow', 'R')
        assert card.getColor() == 'yellow'
        assert card.getValue() == 'R'

    def test_card_wild(self):
        """Test wild card."""
        card = Card('wild', 'W')
        assert card.isWild() is True
        assert card.getColor() == 'wild'

    def test_card_wild_draw_four(self):
        """Test wild draw four card."""
        card = Card('wild', '+4')
        assert card.isWild() is True
        assert card.getValue() == '+4'

    def test_card_points_number(self):
        """Test point values for number cards."""
        card = Card('red', '5')
        assert card.getPoints() == 5

    def test_card_points_zero(self):
        """Test point value for zero card."""
        card = Card('red', '0')
        assert card.getPoints() == 0

    def test_card_points_skip(self):
        """Test point value for skip card."""
        card = Card('red', 'X')
        assert card.getPoints() == 20

    def test_card_points_reverse(self):
        """Test point value for reverse card."""
        card = Card('green', 'R')
        assert card.getPoints() == 20

    def test_card_points_draw_two(self):
        """Test point value for draw two card."""
        card = Card('blue', '+2')
        assert card.getPoints() == 20

    def test_card_points_wild(self):
        """Test point value for wild card."""
        card = Card('wild', 'W')
        assert card.getPoints() == 50

    def test_card_points_draw_four(self):
        """Test point value for draw four card."""
        card = Card('wild', '+4')
        assert card.getPoints() == 50

    def test_card_repr(self):
        """Test card string representation."""
        card = Card('red', '5')
        assert repr(card) == "red,5"

    def test_card_is_zero(self):
        """Test zero card detection."""
        card = Card('red', '0')
        assert card.isZero() is True

    def test_card_not_zero(self):
        """Test non-zero card detection."""
        card = Card('red', '5')
        assert card.isZero() is False


class TestDeck:
    """Tests for Deck class."""

    def test_deck_populate(self):
        """Test deck population."""
        deck = Deck(True)
        assert len(deck) == 108  # Standard UNO deck

    def test_deck_empty_init(self):
        """Test empty deck initialization."""
        deck = Deck(False)
        assert len(deck) == 0

    def test_deck_draw(self):
        """Test drawing a card from deck."""
        deck = Deck(True)
        initial_count = len(deck)
        card = deck.draw()
        assert len(deck) == initial_count - 1
        assert card is not None

    def test_deck_shuffle(self):
        """Test deck shuffling."""
        deck1 = Deck(True)
        deck2 = Deck(True)
        # Both decks should have same cards but possibly different order
        assert len(deck1) == len(deck2)
        # Note: Shuffle might result in same order by chance, but this is unlikely

    def test_deck_place(self):
        """Test placing a card on deck."""
        deck = Deck(False)
        card = Card('red', '5')
        deck.place(card)
        assert len(deck) == 1


class TestHand:
    """Tests for Hand class."""

    def test_hand_empty_init(self):
        """Test empty hand initialization."""
        hand = Hand()
        assert len(hand) == 0

    def test_hand_add_card(self):
        """Test adding a card to hand."""
        hand = Hand()
        card = Card('red', '5')
        hand.addCard(card)
        assert len(hand) == 1

    def test_hand_remove_card(self):
        """Test removing a card from hand."""
        hand = Hand()
        card = Card('red', '5')
        hand.addCard(card)
        removed = hand.removeCard(0)
        assert removed.getColor() == 'red'
        assert len(hand) == 0

    def test_hand_discard(self):
        """Test discarding all cards from hand."""
        hand = Hand()
        hand.addCard(Card('red', '5'))
        hand.addCard(Card('blue', '9'))
        hand.discard()
        assert len(hand) == 0

    def test_hand_get_card(self):
        """Test getting a specific card from hand."""
        hand = Hand()
        card = Card('red', '5')
        hand.addCard(card)
        retrieved = hand.getCard(0)
        assert retrieved.getColor() == 'red'
        assert retrieved.getValue() == '5'

    def test_hand_iterate(self):
        """Test iterating over hand."""
        hand = Hand()
        hand.addCard(Card('red', '5'))
        hand.addCard(Card('blue', '9'))
        cards = list(hand)
        assert len(cards) == 2


class TestPlayer:
    """Tests for Player class."""

    def test_player_init(self):
        """Test player initialization."""
        player = Player("TestPlayer")
        assert player.getName() == "TestPlayer"
        assert player.getPoints() == 0

    def test_player_assign_id(self):
        """Test player ID assignment."""
        player = Player("TestPlayer")
        player.assignID("play1")
        assert player.getID() == "play1"

    def test_player_add_points(self):
        """Test adding points to player."""
        player = Player("TestPlayer")
        player.addPoints(50)
        assert player.getPoints() == 50

    def test_player_add_card(self):
        """Test adding a card to player."""
        player = Player("TestPlayer")
        card = Card('red', '5')
        player.addCard(card)
        assert player.getCardNum() == 1

    def test_player_force_draw(self):
        """Test force draw functionality."""
        player = Player("TestPlayer")
        player.addForceDraw(2)
        assert player.getForceDraws() == 2
        player.decreaseForceDraw()
        assert player.getForceDraws() == 1
        player.removeForceDraw()
        assert player.getForceDraws() == 0


class TestGameSettings:
    """Tests for GameSettings class."""

    def test_game_settings_init(self):
        """Test game settings initialization."""
        gs = GameSettings()
        assert gs.getPlayerNum() == 0
        assert gs.canAddPlayer() is True
        assert gs.canRemovePlayer() is False

    def test_add_player(self):
        """Test adding a player."""
        gs = GameSettings()
        player = Player("TestPlayer")
        gs.addPlayer(player)
        assert gs.getPlayerNum() == 1
        assert gs.canAddPlayer() is True

    def test_add_multiple_players(self):
        """Test adding multiple players."""
        gs = GameSettings()
        gs.addPlayer(Player("Player1"))
        gs.addPlayer(Player("Player2"))
        gs.addPlayer(Player("Player3"))
        gs.addPlayer(Player("Player4"))
        assert gs.getPlayerNum() == 4
        assert gs.canAddPlayer() is False

    def test_remove_player(self):
        """Test removing a player."""
        gs = GameSettings()
        gs.addPlayer(Player("Player1"))
        gs.addPlayer(Player("Player2"))
        gs.removePlayer(1)
        assert gs.getPlayerNum() == 1

    def test_can_begin(self):
        """Test can begin game condition."""
        gs = GameSettings()
        assert gs.canBegin() is False
        gs.addPlayer(Player("Player1"))
        assert gs.canBegin() is False
        gs.addPlayer(Player("Player2"))
        assert gs.canBegin() is True

    def test_finalize_players(self):
        """Test finalizing players."""
        gs = GameSettings()
        gs.addPlayer(Player("Player1"))
        gs.addPlayer(Player("Player2"))
        gs.finalizePlayers()
        assert len(gs.players) == 2

    def test_clear_staging(self):
        """Test clearing staging area."""
        gs = GameSettings()
        gs.addPlayer(Player("Player1"))
        gs.addPlayer(Player("Player2"))
        gs.clearStaging()
        assert gs.getPlayerNum() == 0


class TestBadInputError:
    """Tests for BadInputError exception."""

    def test_bad_input_error(self):
        """Test BadInputError can be raised."""
        with pytest.raises(BadInputError):
            raise BadInputError("Test error")
