-- Type 21 record table (BLPU)
CREATE TABLE blpu (
	record_identifier smallint,
	change_type varchar(1),
	pro_order bigint,
	uprn bigint,
	logical_status smallint,
	blpu_state smallint,
	blpu_state_date date,
	parent_uprn bigint,
	x_coordinate double precision,
	y_coordinate double precision,
	latitude double precision,
	longitude double precision,
	rpc smallint,
	local_custodian_code smallint,
	country varchar(1),
	start_date date,
	end_date date,
	last_update_date date,
	entry_date date,
	addressbase_postal varchar(1),
	postcode_locator varchar(8),
	multi_occ_count smallint
);

-- Type 24 record table (LPI)
CREATE TABLE lpi (
	record_identifier smallint,
	change_type varchar(1),
	pro_order bigint,
	uprn bigint,
	lpi_key varchar(14),
	"language" varchar(3),
	logical_status smallint,
	start_date date,
	end_date date,
	last_update_date date,
	entry_date date,
	sao_start_number smallint,
	sao_start_suffix varchar(2),
	sao_end_number smallint,
	sao_end_suffix varchar(2),
	sao_text varchar(400),
	pao_start_number smallint,
	pao_start_suffix varchar(2),
	pao_end_number smallint,
	pao_end_suffix varchar(2),
	pao_text varchar(90),
	usrn integer,
	usrn_match_indicator varchar(1),
	area_name varchar(100),
	"level" varchar(30),
	official_flag varchar(1)
);

-- Type 32 record table (CLASSIFICATION)
CREATE TABLE classification (
	record_identifier smallint,
	change_type varchar(1),
	pro_order bigint,
	uprn bigint,
	class_key varchar(14),
	classification_code varchar(6),
	class_scheme varchar(60),
	scheme_version double precision,
	start_date date,
	end_date date,
	last_update_date date,
	entry_date date
);
