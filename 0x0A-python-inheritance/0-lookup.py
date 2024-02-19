#!/usr/bin/python3

"""Defines aan object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attribute."""
    return (dir(obj));
