init 5 python:
    list_of_instantiation_labels.append("add_extra_room_job_definitions")

label add_extra_room_job_definitions():
    # runs right after the base game jobs have been created
    python:
        barista_coffee_shop_job = Job("Barista", unimportant_job_role, job_location = coffee_shop, work_days = [0,1,2,3,4,5], work_times = [1,2])
        list_of_jobs.append([barista_coffee_shop_job, 3])

        yoga_teacher_job = Job("Yoga Teacher", unimportant_job_role, job_location = gym, work_days = [0,1,2,3,4], work_times = [2,3])
        list_of_jobs.append([yoga_teacher_job, 3])

        bartender_downtown_bar_job = Job("Bartender", unimportant_job_role, job_location = downtown_bar, work_days = [2,3,4,5,6], work_times = [3,4])
        waitress_downtown_bar_job = Job("Waitress", unimportant_job_role, job_location = downtown_bar, work_days = [2,3,4,5,6], work_times = [3,4])
        list_of_jobs.append([bartender_downtown_bar_job, 3])
        list_of_jobs.append([waitress_downtown_bar_job, 3])

        receptionist_hotel_job = Job("Receptionist", unimportant_job_role, job_location = downtown_hotel, work_days = [2,3,4,5,6], work_times = [1,2])
        maid_hotel_job = Job("Maid", unimportant_job_role, job_location = downtown_hotel, work_days = [0,2,4,6], work_times=[1,2])
        maid_hotel_job2 = Job("Maid", unimportant_job_role, job_location = downtown_hotel, work_days = [1,3,5], work_times=[1,2,3])
        chef_hotel_job = Job("Chef", unimportant_job_role, job_location = downtown_hotel, work_days = [0,2,3,4,5,6], work_times = [2, 3])
        list_of_jobs.append([receptionist_hotel_job, 3])
        list_of_jobs.append([maid_hotel_job, 5])
        list_of_jobs.append([maid_hotel_job2, 5])
        list_of_jobs.append([chef_hotel_job, 3])

        hairdresser_salon_job = Job("Hairdresser", unimportant_job_role, job_location = mall_salon, work_days=[1,2,3,4,5], work_times = [1, 2])
        list_of_jobs.append([hairdresser_salon_job, 3])

        home_improvement_support_job = Job("Customer Support", unimportant_job_role, job_location = home_store, work_days = [0,1,2,3,4], work_times = [1,2])
        electronics_support_job = Job("Customer Support", unimportant_job_role, job_location = electronics_store, work_days = [0,1,2,3,4], work_times = [1,2])
        store_assistant_job = Job("Store Assistant", unimportant_job_role, job_location = mall, work_days = [0,1,2,3,4], work_times = [1,2])
        store_clerk_job = Job("Store Clerk", unimportant_job_role, job_location = office_store, work_days = [0,1,2,3,4], work_times = [1,2])
        list_of_jobs.append([home_improvement_support_job, 5])
        list_of_jobs.append([electronics_support_job, 5])
        list_of_jobs.append([store_assistant_job, 5])
        list_of_jobs.append([store_clerk_job, 5])

        lawyer_job = Job("Lawyer", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        doctor_job = Job("Doctor", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        architect_job = Job("Architect", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        interior_decorator_job = Job("Interior Decorator", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        fashion_designer_job = Job("Fashion Designer", critical_job_role, job_location = downtown, work_days = [0,1,2,3,4], work_times = [1,2])
        pro_gamer_job = Job("Pro Gamer", critical_job_role, job_location = gaming_cafe, work_days = [2,4,5,6], work_times = [2, 3])

        list_of_jobs.append([lawyer_job, 2])
        list_of_jobs.append([doctor_job, 2])
        list_of_jobs.append([architect_job, 2])
        list_of_jobs.append([interior_decorator_job, 2])
        list_of_jobs.append([fashion_designer_job, 2])
        list_of_jobs.append([pro_gamer_job, 2])

        # shuffle the list of jobs
        renpy.random.shuffle(list_of_jobs)
    return
