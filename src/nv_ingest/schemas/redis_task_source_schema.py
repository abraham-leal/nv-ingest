# SPDX-FileCopyrightText: Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from pydantic import Field, BaseModel

from nv_ingest.schemas.redis_client_schema import RedisClientSchema
from typing_extensions import Annotated


class RedisTaskSourceSchema(BaseModel):
    redis_client: RedisClientSchema = RedisClientSchema()
    task_queue: str = "morpheus_task_queue"

    progress_engines: Annotated[int, Field(ge=1)] = 6
