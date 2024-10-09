# SPDX-FileCopyrightText: Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import Optional

from pydantic import Field, BaseModel
from typing_extensions import Annotated


class RedisClientSchema(BaseModel):
    host: str = "redis"
    port: Annotated[int, Field(gt=0, lt=65536)] = 6379  # Ports must be in the range 1-65535
    use_ssl: Optional[bool] = False

    connection_timeout: Optional[Annotated[int, Field(ge=0)]] = 300
    max_backoff: Optional[Annotated[int, Field(ge=0)]] = 300
    max_retries: Optional[Annotated[int, Field(ge=0)]] = 0
