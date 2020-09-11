#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aws_lambda_powertools import Logger
import boto3
import botocore

logger = Logger(child=True)

__all__ = ["ServiceCatalog"]


class ServiceCatalog:
    def __init__(self) -> None:
        self.client = boto3.client("servicecatalog")

    def enable_aws_organizations_access(self) -> None:
        logger.info("Enabling organizational access for ServiceCatalog")
        try:
            self.client.enable_aws_organizations_access()
            logger.debug("Enabled organizational access for ServiceCatalog")
        except botocore.exceptions.ClientError as error:
            if error.response["Error"]["Code"] != "InvalidStateException":
                logger.exception("Unable enable organization access for ServiceCatalog")
                raise error
