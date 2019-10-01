# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CachingRuleSummary(object):
    """
    The caching rule settings.
    """

    #: A constant which can be used with the action property of a CachingRuleSummary.
    #: This constant has a value of "CACHE"
    ACTION_CACHE = "CACHE"

    #: A constant which can be used with the action property of a CachingRuleSummary.
    #: This constant has a value of "BYPASS_CACHE"
    ACTION_BYPASS_CACHE = "BYPASS_CACHE"

    def __init__(self, **kwargs):
        """
        Initializes a new CachingRuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CachingRuleSummary.
        :type key: str

        :param name:
            The value to assign to the name property of this CachingRuleSummary.
        :type name: str

        :param action:
            The value to assign to the action property of this CachingRuleSummary.
            Allowed values for this property are: "CACHE", "BYPASS_CACHE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param caching_duration:
            The value to assign to the caching_duration property of this CachingRuleSummary.
        :type caching_duration: str

        :param is_client_caching_enabled:
            The value to assign to the is_client_caching_enabled property of this CachingRuleSummary.
        :type is_client_caching_enabled: bool

        :param client_caching_duration:
            The value to assign to the client_caching_duration property of this CachingRuleSummary.
        :type client_caching_duration: str

        :param criteria:
            The value to assign to the criteria property of this CachingRuleSummary.
        :type criteria: list[CachingRuleCriteria]

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'action': 'str',
            'caching_duration': 'str',
            'is_client_caching_enabled': 'bool',
            'client_caching_duration': 'str',
            'criteria': 'list[CachingRuleCriteria]'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'action': 'action',
            'caching_duration': 'cachingDuration',
            'is_client_caching_enabled': 'isClientCachingEnabled',
            'client_caching_duration': 'clientCachingDuration',
            'criteria': 'criteria'
        }

        self._key = None
        self._name = None
        self._action = None
        self._caching_duration = None
        self._is_client_caching_enabled = None
        self._client_caching_duration = None
        self._criteria = None

    @property
    def key(self):
        """
        Gets the key of this CachingRuleSummary.
        The unique key for the caching rule.


        :return: The key of this CachingRuleSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CachingRuleSummary.
        The unique key for the caching rule.


        :param key: The key of this CachingRuleSummary.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CachingRuleSummary.
        The name of the caching rule.


        :return: The name of this CachingRuleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CachingRuleSummary.
        The name of the caching rule.


        :param name: The name of this CachingRuleSummary.
        :type: str
        """
        self._name = name

    @property
    def action(self):
        """
        **[Required]** Gets the action of this CachingRuleSummary.
        The action to take on matched caching rules.
        - **CACHE:** Allow to set caching rule, which would be cached.

        - **BYPASS_CACHE:** Allow to set caching rule, which would never be cached. e.g. all requests would be passed directly to origin for those file types.

        Allowed values for this property are: "CACHE", "BYPASS_CACHE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this CachingRuleSummary.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this CachingRuleSummary.
        The action to take on matched caching rules.
        - **CACHE:** Allow to set caching rule, which would be cached.

        - **BYPASS_CACHE:** Allow to set caching rule, which would never be cached. e.g. all requests would be passed directly to origin for those file types.


        :param action: The action of this CachingRuleSummary.
        :type: str
        """
        allowed_values = ["CACHE", "BYPASS_CACHE"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def caching_duration(self):
        """
        Gets the caching_duration of this CachingRuleSummary.
        The caching duration (applies only to `CACHE` action) specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days, weeks, months. Max value - 99. Mixing of multiple units is not supported.


        :return: The caching_duration of this CachingRuleSummary.
        :rtype: str
        """
        return self._caching_duration

    @caching_duration.setter
    def caching_duration(self, caching_duration):
        """
        Sets the caching_duration of this CachingRuleSummary.
        The caching duration (applies only to `CACHE` action) specified in ISO 8601 extended format. Supported units: seconds, minutes, hours, days, weeks, months. Max value - 99. Mixing of multiple units is not supported.


        :param caching_duration: The caching_duration of this CachingRuleSummary.
        :type: str
        """
        self._caching_duration = caching_duration

    @property
    def is_client_caching_enabled(self):
        """
        Gets the is_client_caching_enabled of this CachingRuleSummary.
        Enables or disables the client caching.
        Browsers use the Cache-Control header value for caching content locally, in the browser.
        This setting will control the addition of a Cache-Control header to responses. It overrides existing Cache-Control headers.


        :return: The is_client_caching_enabled of this CachingRuleSummary.
        :rtype: bool
        """
        return self._is_client_caching_enabled

    @is_client_caching_enabled.setter
    def is_client_caching_enabled(self, is_client_caching_enabled):
        """
        Sets the is_client_caching_enabled of this CachingRuleSummary.
        Enables or disables the client caching.
        Browsers use the Cache-Control header value for caching content locally, in the browser.
        This setting will control the addition of a Cache-Control header to responses. It overrides existing Cache-Control headers.


        :param is_client_caching_enabled: The is_client_caching_enabled of this CachingRuleSummary.
        :type: bool
        """
        self._is_client_caching_enabled = is_client_caching_enabled

    @property
    def client_caching_duration(self):
        """
        Gets the client_caching_duration of this CachingRuleSummary.
        The client caching duration (applies only to `CACHE` action) specified in ISO 8601 extended format, in case client caching enabled. It sets Cache-Control header max-age time, i.e. the local browser cache expire time. Supported units: seconds, minutes, hours, days, weeks, months. Max value - 99. Mixing of multiple units is not supported.


        :return: The client_caching_duration of this CachingRuleSummary.
        :rtype: str
        """
        return self._client_caching_duration

    @client_caching_duration.setter
    def client_caching_duration(self, client_caching_duration):
        """
        Sets the client_caching_duration of this CachingRuleSummary.
        The client caching duration (applies only to `CACHE` action) specified in ISO 8601 extended format, in case client caching enabled. It sets Cache-Control header max-age time, i.e. the local browser cache expire time. Supported units: seconds, minutes, hours, days, weeks, months. Max value - 99. Mixing of multiple units is not supported.


        :param client_caching_duration: The client_caching_duration of this CachingRuleSummary.
        :type: str
        """
        self._client_caching_duration = client_caching_duration

    @property
    def criteria(self):
        """
        **[Required]** Gets the criteria of this CachingRuleSummary.
        The array of the rule criteria with condition and value.


        :return: The criteria of this CachingRuleSummary.
        :rtype: list[CachingRuleCriteria]
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """
        Sets the criteria of this CachingRuleSummary.
        The array of the rule criteria with condition and value.


        :param criteria: The criteria of this CachingRuleSummary.
        :type: list[CachingRuleCriteria]
        """
        self._criteria = criteria

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other