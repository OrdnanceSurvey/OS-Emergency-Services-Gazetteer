-- Type 21 record table (BLPU)
CREATE TABLE blpu (
	record_identifier smallint,
	change_type nvarchar(1),
	pro_order bigint,
	uprn bigint,
	logical_status smallint,
	blpu_state smallint,
	blpu_state_date date,
	parent_uprn bigint,
	x_coordinate float(53),
	y_coordinate float(53),
	latitude float(53),
	longitude float(53),
	rpc smallint,
	local_custodian_code smallint,
	country nvarchar(1),
	start_date date,
	end_date date,
	last_update_date date,
	entry_date date,
	addressbase_postal nvarchar(1),
	postcode_locator nvarchar(8),
	multi_occ_count smallint
);

-- Type 24 record table (LPI)
CREATE TABLE lpi (
	record_identifier smallint,
	change_type nvarchar(1),
	pro_order bigint,
	uprn bigint,
	lpi_key nvarchar(14),
	"language" nvarchar(3),
	logical_status smallint,
	start_date date,
	end_date date,
	last_update_date date,
	entry_date date,
	sao_start_number smallint,
	sao_start_suffix nvarchar(2),
	sao_end_number smallint,
	sao_end_suffix nvarchar(2),
	sao_text nvarchar(90),
	pao_start_number smallint,
	pao_start_suffix nvarchar(2),
	pao_end_number smallint,
	pao_end_suffix nvarchar(2),
	pao_text nvarchar(90),
	usrn integer,
	usrn_match_indicator nvarchar(1),
	area_name nvarchar(35),
	"level" nvarchar(30),
	official_flag nvarchar(1)
);

-- Type 32 record table (CLASSIFICATION)
CREATE TABLE classification (
	record_identifier smallint,
	change_type nvarchar(1),
	pro_order bigint,
	uprn bigint,
	class_key nvarchar(14),
	classification_code nvarchar(6),
	class_scheme nvarchar(60),
	scheme_version float(53),
	start_date date,
	end_date date,
	last_update_date date,
	entry_date date
);
